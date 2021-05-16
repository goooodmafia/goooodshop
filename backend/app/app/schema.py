from django.core.paginator import Paginator
from django.db.models import Q, F, Count, Value, BooleanField, CharField

import graphene
from graphene_django_extras import DjangoFilterListField, DjangoFilterPaginateListField, LimitOffsetGraphqlPagination, \
    DjangoListObjectField

from content.models import Content
from news.models import News
from news.schema import NewsType
from shop.enums import OrderEnum, GrapheneOrderEnum
from shop.models import Category, Product
from shop.schema import CategoryType, ProductType, ProductListType, ProductFilter, FiltersType

from content.schema import ContentType
from content.schema import PositionEnum
from users.schema import Query as AuthQuery
from users.schema import Mutations as AuthMutations
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def get_paginator(qs, page, page_size, paginated_type, **kwargs):
    p = Paginator(qs, page_size)
    try:
        page_obj = p.page(page)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return paginated_type(
        items=page_obj.object_list,
        total=qs.count(),
        # page=page_obj.number,
        pages=p.num_pages,
        has_next=page_obj.has_next(),
        has_prev=page_obj.has_previous(),
        **kwargs
    )


class CountableType(graphene.ObjectType):
    total = graphene.Int()
    # page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()


class ProductCountableType(CountableType):
    items = graphene.List(ProductType)
    filters = graphene.List(FiltersType)


class MyQuery(graphene.ObjectType):
    content = graphene.List(ContentType, route=graphene.String(), position=PositionEnum())
    category = graphene.Field(CategoryType, route=graphene.String())
    categories = graphene.List(CategoryType)

    product = graphene.Field(ProductType, sku=graphene.String())

    news = graphene.List(
        NewsType,
        per_page=graphene.Argument(graphene.Int),
        page=graphene.Argument(graphene.Int)
    )

    def resolve_news(self, info, per_page, page):
        qs = News.objects.filter(enable=True)
        qs = Paginator(qs, per_page).page(page)
        return qs

    newscount = graphene.Int()

    def resolve_newscount(self, info):
        return News.objects.filter(enable=True).count()

    products = graphene.Field(
        ProductCountableType,
        page=graphene.Argument(graphene.Int),
        page_size=graphene.Argument(graphene.Int),
        route=graphene.Argument(graphene.String),
        colors=graphene.Argument(graphene.String),
        sizes=graphene.Argument(graphene.String),
        effects=graphene.Argument(graphene.String),
        tags=graphene.Argument(graphene.String),
        hit=graphene.Argument(graphene.Boolean),
        new=graphene.Argument(graphene.Boolean),
        query=graphene.Argument(graphene.String),
        order=graphene.Argument(GrapheneOrderEnum)
    )

    def resolve_products(
            self,
            info,
            page,
            page_size,
            route,
            sizes,
            colors,
            effects,
            tags,
            hit,
            new,
            query,
            order
    ):
        route_filter = Q(categories__path__icontains=route)

        sizes_list = list(filter(None, map(str.strip, sizes.split(','))))
        all_sizes_list = {
            'size_ns': 'Без размера',
            'size_xs': 'XS',
            'size_s': 'S',
            'size_m': 'M',
            'size_l': 'L',
            'size_xl': 'XL',
            'size_2xl': 'XXL',
            'size_3xl': 'XXXL',
            'size_4xl': 'XXXXL',
        }
        all_sizes_list_rev = dict(zip(all_sizes_list.values(), all_sizes_list.keys()))
        avaliable_sizes = [all_sizes_list_rev[key] for key in sizes_list]

        sizes_filter = Q()
        for size in avaliable_sizes:
            sizes_filter |= Q(**{size + '__gt': 0})

        color_list = list(filter(None, map(str.strip, colors.split(','))))
        color_filter = Q(colors__name__in=color_list) if color_list else Q()

        effects_list = list(filter(None, map(str.strip, effects.split(','))))
        effect_glow_in_the_dark = 'Светится в темноте' in effects_list
        effect_glow_in_the_uv = 'Светится в ультрафиолете' in effects_list
        effects_filter = Q()
        if effect_glow_in_the_dark:
            effects_filter = effects_filter & Q(glow_in_the_dark=True)
        if effect_glow_in_the_uv:
            effects_filter = effects_filter & Q(glow_in_the_uv=True)

        tag_list = list(filter(None, map(str.strip, tags.split(','))))
        tag_filter = Q(tags__name__in=tag_list) if tag_list else Q()

        hit_filter = Q()
        if hit:
            hit_filter = hit_filter & Q(hit=True)
        new_filter = Q()
        if hit:
            new_filter = new_filter & Q(hit=True)

        query_filter = Q(translations__description__icontains=query) \
                       | Q(model__icontains=query) \
                       | Q(sku__icontains=query)

        pqs = Product.objects.filter(enable=True, total_count__gt=0)
        pqs = pqs.filter(route_filter)
        pqs = pqs.filter(query_filter)
        pqs = pqs.filter(hit_filter)
        pqs = pqs.filter(new_filter)

        qs = pqs.filter(color_filter)
        qs = qs.filter(effects_filter)
        qs = qs.filter(sizes_filter)
        qs = qs.filter(tag_filter)
        qs = qs.distinct()

        sizes_qs = [
            {'lable': value,
             'count': pqs.filter(effects_filter & color_filter).values(key).filter(Q(**{key + '__gt': 0})).count()
             # 'value': True if key in avaliable_sizes else False
             } for key, value in all_sizes_list.items()
        ]

        color_qs = pqs \
            .annotate(lable=F('colors__name')).values('lable') \
            .exclude(lable__isnull=True) \
            .annotate(count=Count('lable', filter=effects_filter & sizes_filter)) \
            .order_by('lable') \
            # .annotate(value=Value(False, output_field=BooleanField())) \

        products_dark_qs = pqs \
            .values('glow_in_the_dark') \
            .filter(glow_in_the_dark=True) \
            .annotate(count=Count('glow_in_the_dark', filter=color_filter & sizes_filter)) \
            .annotate(lable=Value('Светится в темноте', output_field=CharField())) \
            .values('lable', 'count')
        # .annotate(value=Value(effect_glow_in_the_dark, output_field=BooleanField())) \
        # .values('lable', 'count', 'value')

        products_uv_qs = pqs \
            .values('glow_in_the_uv') \
            .filter(glow_in_the_uv=True) \
            .annotate(count=Count('glow_in_the_uv', filter=color_filter & sizes_filter)) \
            .annotate(lable=Value('Светится в ультрафиолете', output_field=CharField())) \
            .values('lable', 'count')
        # .annotate(value=Value(effect_glow_in_the_uv, output_field=BooleanField())) \
        # .values('lable', 'count', 'value')

        colors = list(color_qs)

        # for color in colors:
        #     if color['lable'] in color_list:
        #         color['value'] = True

        filters = [
            FiltersType(title='Размер', name='size', items=sizes_qs),
            FiltersType(title='Цвет', name='color', items=colors),
            FiltersType(title='Спецэффекты', name='effects', items=list(products_dark_qs) + list(products_uv_qs)),
        ]

        if order == OrderEnum.Random.value: qs = qs.order_by('?')
        if order == OrderEnum.OrderInc.value: qs = qs.order_by('my_order')
        if order == OrderEnum.OrderDec.value: qs = qs.order_by('-my_order')
        if order == OrderEnum.PriceInc.value: qs = qs.order_by('price_ret', 'my_order')
        if order == OrderEnum.PriceDec.value: qs = qs.order_by('-price_ret', 'my_order')
        if order == OrderEnum.SaleInc.value: qs = qs.order_by('sale', 'my_order')
        if order == OrderEnum.SaleDec.value: qs = qs.order_by('-sale', 'my_order')
        # if order == OrderEnum.HitInc.value: qs = qs.order_by('hit', 'my_order')
        # if order == OrderEnum.HitDec.value: qs = qs.order_by('-hit', 'my_order')

        return get_paginator(qs, page, page_size, ProductCountableType, filters=filters)

    # fetchproducts = graphene.List(
    #     ProductType,
    #     per_page=graphene.Argument(graphene.Int),
    #     page=graphene.Argument(graphene.Int),
    #     route=graphene.Argument(graphene.String),
    #     colors=graphene.Argument(graphene.String),
    #     sizes=graphene.Argument(graphene.String),
    #     effects=graphene.Argument(graphene.String),
    #     tags=graphene.Argument(graphene.String),
    #     query=graphene.Argument(graphene.String),
    #     order=graphene.Argument(GrapheneOrderEnum)
    # )
    #
    # fetchproductscount = graphene.Int(
    #     route=graphene.Argument(graphene.String),
    #     sizes=graphene.Argument(graphene.String),
    #     colors=graphene.Argument(graphene.String),
    #     effects=graphene.Argument(graphene.String),
    #     query=graphene.Argument(graphene.String)
    # )
    #
    # filters = graphene.List(
    #     FiltersType,
    #     route=graphene.Argument(graphene.String),
    #     sizes=graphene.Argument(graphene.String),
    #     colors=graphene.Argument(graphene.String),
    #     effects=graphene.Argument(graphene.String),
    #     query=graphene.Argument(graphene.String)
    # )

    def resolve_content(self, info, route, position):
        return Content.objects.filter(enable=True, route=route, position=position)

    def resolve_category(self, info, route):
        try:
            return Category.objects.get(enable=True, path=route)
        except Category.DoesNotExist:
            return None

    def resolve_categories(self, info):
        return Category.objects.filter(enable=True, parent=None) \
            .annotate(
            num_children=Count(
                'children',
                filter=Q(children__products__total_count__gt=0)
            )
        ).filter(num_children__gt=0)

    def resolve_product(self, info, sku):
        return Product.objects.get(sku=sku)

    def resolve_filters(self, info, route, sizes, colors, effects, query):
        print(sizes)
        colors_list = list(filter(None, map(str.strip, colors.split(','))))
        effects_list = list(filter(None, map(str.strip, effects.split(','))))

        effect_glow_in_the_dark = 'Светится в темноте' in effects_list
        effect_glow_in_the_uv = 'Светится в ультрафиолете' in effects_list

        sizes_list = list(filter(None, map(str.strip, sizes.split(','))))
        s_list = {
            'size_ns': 'Без размера',
            'size_xs': 'XS',
            'size_s': 'S',
            'size_m': 'M',
            'size_l': 'L',
            'size_xl': 'XL',
            'size_2xl': 'XXL',
            'size_3xl': 'XXXL',
            'size_4xl': 'XXXXL',
        }
        s_list_rev = dict(zip(s_list.values(), s_list.keys()))
        s = [s_list_rev[key] for key in sizes_list]

        sizes_filter = Q()
        for size in s:
            sizes_filter |= Q(**{size + '__gt': 0})

        colors_filter = Q()
        if len(colors_list) > 0:
            colors_filter = colors_filter & Q(colors__name__in=colors_list)

        effects_filter = Q()
        if effect_glow_in_the_dark:
            effects_filter = effects_filter & Q(glow_in_the_dark=True)
        if effect_glow_in_the_uv:
            effects_filter = effects_filter & Q(glow_in_the_uv=True)

        query_filter = Q(translations__description__icontains=query) \
                       | Q(model__icontains=query) \
                       | Q(sku__icontains=query)

        qs = Product.objects.filter(enable=True, total_count__gt=0)
        qs = qs.filter(categories__path__icontains=route)
        qs = qs.filter(query_filter)
        # qs = qs.distinct()

        sizes_qs = qs \
            .filter(colors_filter) \
            .filter(effects_filter)

        sizes_qs = [
            {'lable': value,
             'count': sizes_qs.values(key).filter(Q(**{key + '__gt': 0})).count(),
             'value': True if key in s else False} for key, value in s_list.items()
        ]

        color_qs = qs \
            .annotate(lable=F('colors__name')).values('lable') \
            .exclude(lable__isnull=True) \
            .annotate(count=Count('lable', filter=effects_filter & sizes_filter)) \
            .annotate(value=Value(False, output_field=BooleanField())) \
            .order_by('lable')

        products_dark_qs = qs \
            .values('glow_in_the_dark') \
            .filter(glow_in_the_dark=True) \
            .annotate(count=Count('glow_in_the_dark', filter=colors_filter & sizes_filter)) \
            .annotate(lable=Value('Светится в темноте', output_field=CharField())) \
            .annotate(value=Value(effect_glow_in_the_dark, output_field=BooleanField())) \
            .values('lable', 'count', 'value')

        products_uv_qs = qs \
            .values('glow_in_the_uv') \
            .filter(glow_in_the_uv=True) \
            .annotate(count=Count('glow_in_the_uv', filter=colors_filter & sizes_filter)) \
            .annotate(lable=Value('Светится в ультрафиолете', output_field=CharField())) \
            .annotate(value=Value(effect_glow_in_the_uv, output_field=BooleanField())) \
            .values('lable', 'count', 'value')

        colors = list(color_qs)

        for color in colors:
            if color['lable'] in colors_list:
                color['value'] = True

        print(sizes_qs)

        return [
            FiltersType(title='Размер', name='size', items=sizes_qs),
            FiltersType(title='Цвет', name='color', items=colors),
            FiltersType(title='Спецэффекты', name='effects', items=list(products_dark_qs) + list(products_uv_qs)),
        ]

    def resolve_fetchproducts(
            self,
            info,
            per_page,
            page,
            route,
            sizes,
            colors,
            effects,
            tags,
            query,
            order
    ):

        route_filter = Q(categories__path__icontains=route)

        sizes_list = list(filter(None, map(str.strip, sizes.split(','))))
        s_list = {
            'size_ns': 'Без размера',
            'size_xs': 'XS',
            'size_s': 'S',
            'size_m': 'M',
            'size_l': 'L',
            'size_xl': 'XL',
            'size_2xl': 'XXL',
            'size_3xl': 'XXXL',
            'size_4xl': 'XXXXL',
        }
        s_list_rev = dict(zip(s_list.values(), s_list.keys()))
        s = [s_list_rev[key] for key in sizes_list]

        sizes_filter = Q()
        for size in s:
            sizes_filter |= Q(**{size + '__gt': 0})

        color_list = list(filter(None, map(str.strip, colors.split(','))))
        color_filter = Q(colors__name__in=color_list) if color_list else Q()

        effects_list = list(filter(None, map(str.strip, effects.split(','))))
        effect_glow_in_the_dark = 'Светится в темноте' in effects_list
        effect_glow_in_the_uv = 'Светится в ультрафиолете' in effects_list
        effects_filter = Q()
        if effect_glow_in_the_dark:
            effects_filter = effects_filter & Q(glow_in_the_dark=True)
        if effect_glow_in_the_uv:
            effects_filter = effects_filter & Q(glow_in_the_uv=True)

        tag_list = list(filter(None, map(str.strip, tags.split(','))))
        tag_filter = Q(tags__name__in=tag_list) if tag_list else Q()

        query_filter = Q(translations__description__icontains=query) \
                       | Q(model__icontains=query) \
                       | Q(sku__icontains=query)

        qs_filter = route_filter \
                    & color_filter \
                    & effects_filter \
                    & sizes_filter \
                    & tag_filter \
                    & query_filter

        qs = Product.objects.filter(enable=True, total_count__gt=0)
        qs = qs.filter(qs_filter)
        qs = qs.distinct()

        if order == OrderEnum.Random.value: qs = qs.order_by('?')
        if order == OrderEnum.OrderInc.value: qs = qs.order_by('my_order')
        if order == OrderEnum.OrderDec.value: qs = qs.order_by('-my_order')
        if order == OrderEnum.PriceInc.value: qs = qs.order_by('price_ret', 'my_order')
        if order == OrderEnum.PriceDec.value: qs = qs.order_by('-price_ret', 'my_order')
        if order == OrderEnum.SaleInc.value: qs = qs.order_by('sale', 'my_order')
        if order == OrderEnum.SaleDec.value: qs = qs.order_by('-sale', 'my_order')
        if order == OrderEnum.HitInc.value: qs = qs.order_by('hit', 'my_order')
        if order == OrderEnum.HitDec.value: qs = qs.order_by('-hit', 'my_order')

        qs = Paginator(qs, per_page).page(page)

        return qs

    def resolve_fetchproductscount(self, info, route, sizes, colors, effects, query):
        qs = Product.objects.filter(enable=True, total_count__gt=0).filter(categories__path__icontains=route)
        # qs = Category.objects.get(path=route).products.filter(enable=True, total_count__gt=0)
        if (colors):
            colors_list = list(map(str.strip, colors.split(',')))
            colors_filter = (
                Q(colors__name__in=colors_list)
            )
            qs = qs.filter(colors_filter)

        effects_list = list(map(str.strip, effects.split(',')))

        effect_glow_in_the_dark = 'Светится в темноте' in effects_list
        effect_glow_in_the_uv = 'Светится в ультрафиолете' in effects_list

        sizes_list = list(filter(None, map(str.strip, sizes.split(','))))
        s_list = {
            'size_ns': 'Без размера',
            'size_xs': 'XS',
            'size_s': 'S',
            'size_m': 'M',
            'size_l': 'L',
            'size_xl': 'XL',
            'size_2xl': 'XXL',
            'size_3xl': 'XXXL',
            'size_4xl': 'XXXXL',
        }
        s_list_rev = dict(zip(s_list.values(), s_list.keys()))
        s = [s_list_rev[key] for key in sizes_list]

        sizes_filter = Q()
        for size in s:
            sizes_filter |= Q(**{size + '__gt': 0})

        effects_filter = Q()
        if effect_glow_in_the_dark:
            effects_filter = effects_filter & Q(glow_in_the_dark=True)
        if effect_glow_in_the_uv:
            effects_filter = effects_filter & Q(glow_in_the_uv=True)

        query_filter = Q(translations__description__icontains=query) \
                       | Q(model__icontains=query) \
                       | Q(sku__icontains=query)

        qs = qs.filter(effects_filter)
        qs = qs.filter(sizes_filter)
        qs = qs.filter(query_filter)
        qs = qs.distinct()
        return qs.count()


class Mutations(AuthMutations, graphene.ObjectType):
    pass


class Query(MyQuery, AuthQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
