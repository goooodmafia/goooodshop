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


class MyQuery(graphene.ObjectType):
    content = graphene.List(ContentType, route=graphene.String(), position=PositionEnum())
    category = graphene.Field(CategoryType, route=graphene.String())
    categories = graphene.List(CategoryType)

    product = graphene.Field(ProductType, sku=graphene.String())

    products = DjangoListObjectField(
        ProductListType,
        filterset_class=ProductFilter
    )

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

    # fetchproducts = DjangoFilterPaginateListField(
    #     ProductType,
    #     pagination=LimitOffsetGraphqlPagination(ordering="?"),
    #     filterset_class=ProductFilter
    # )

    fetchproducts = graphene.List(
        ProductType,
        per_page=graphene.Argument(graphene.Int),
        page=graphene.Argument(graphene.Int),
        route=graphene.Argument(graphene.String),
        colors=graphene.Argument(graphene.String),
        effects=graphene.Argument(graphene.String),
        tags=graphene.Argument(graphene.String),
        query=graphene.Argument(graphene.String),
        order=graphene.Argument(GrapheneOrderEnum)
    )

    fetchproductscount = graphene.Int(
        route=graphene.Argument(graphene.String),
        colors=graphene.Argument(graphene.String),
        effects=graphene.Argument(graphene.String)
    )

    filters = graphene.List(
        FiltersType,
        route=graphene.Argument(graphene.String),
        sizes=graphene.Argument(graphene.String),
        colors=graphene.Argument(graphene.String),
        effects=graphene.Argument(graphene.String)
    )

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

    def resolve_filters(self, info, route, sizes, colors, effects):

        sizes_list = list(filter(None, map(str.strip, sizes.split(','))))
        colors_list = list(filter(None, map(str.strip, colors.split(','))))
        effects_list = list(filter(None, map(str.strip, effects.split(','))))

        effect_glow_in_the_dark = 'Светится в темноте' in effects_list
        effect_glow_in_the_uv = 'Светится в ультрафиолете' in effects_list

        sizes_filter = Q()

        print(sizes_list)

        for size in sizes_list:
            sizes_filter |= Q(**{size + '__gt': 0})

        print(sizes_filter)

        colors_filter = Q()
        if len(colors_list) > 0:
            colors_filter = colors_filter & Q(colors__name__in=colors_list)

        effects_filter = Q()
        if effect_glow_in_the_dark:
            effects_filter = effects_filter & Q(glow_in_the_dark=True)
        if effect_glow_in_the_uv:
            effects_filter = effects_filter & Q(glow_in_the_uv=True)

        products_qs = Product.objects.filter(categories__path__icontains=route)

        sizes_qs = products_qs
        # .filter(colors_filter) \
        # .filter(effects_filter)

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

        sizes = [
            {'lable': value,
             'count': sizes_qs.values(key).filter(Q(**{key + '__gt': 0})).count(),
             'value': False} for (key, value) in s_list.items()
        ]
        #
        # print(sizes_qs.values('size_ns').filter(Q(**{'size_ns' + '__gt': 0})).count())
        #
        # print(s)

        color_qs = products_qs \
            .annotate(lable=F('colors__name')).values('lable') \
            .exclude(lable__isnull=True) \
            .annotate(count=Count('lable', filter=effects_filter)) \
            .annotate(value=Value(False, output_field=BooleanField())) \
            .order_by('lable')

        products_dark_qs = products_qs \
            .values('glow_in_the_dark') \
            .filter(glow_in_the_dark=True) \
            .annotate(count=Count('glow_in_the_dark', filter=colors_filter)) \
            .annotate(lable=Value('Светится в темноте', output_field=CharField())) \
            .annotate(value=Value(effect_glow_in_the_dark, output_field=BooleanField())) \
            .values('lable', 'count', 'value')

        products_uv_qs = products_qs \
            .values('glow_in_the_uv') \
            .filter(glow_in_the_uv=True) \
            .annotate(count=Count('glow_in_the_uv', filter=colors_filter)) \
            .annotate(lable=Value('Светится в ультрафиолете', output_field=CharField())) \
            .annotate(value=Value(effect_glow_in_the_uv, output_field=BooleanField())) \
            .values('lable', 'count', 'value')

        colors = list(color_qs)

        for color in colors:
            if color['lable'] in colors_list:
                color['value'] = True

        return [
            FiltersType(title='Размер', name='size', items=sizes),
            FiltersType(title='Цвет', name='color', items=colors),
            FiltersType(title='Спецэффекты', name='effects', items=list(products_dark_qs) + list(products_uv_qs)),
        ]

    def resolve_fetchproducts(self, info, per_page, page, route, colors, effects, tags, query, order):

        route_filter = Q(categories__path__icontains=route)

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
                    & tag_filter \
                    & query_filter

        qs = Product.objects.all()
        qs = qs.filter(qs_filter)

        if order == OrderEnum.Random.value: qs = qs.order_by('?')
        if order == OrderEnum.OrderInc.value: qs = qs.order_by('my_order')
        if order == OrderEnum.OrderDec.value: qs = qs.order_by('-my_order')
        if order == OrderEnum.PriceInc.value: qs = qs.order_by('price_ret', 'my_order')
        if order == OrderEnum.PriceDec.value: qs = qs.order_by('-price_ret', 'my_order')
        if order == OrderEnum.SaleInc.value: qs = qs.order_by('sale', 'my_order')
        if order == OrderEnum.SaleDec.value: qs = qs.order_by('-sale', 'my_order')

        qs = Paginator(qs, per_page).page(page)

        return qs

    def resolve_fetchproductscount(self, info, route, colors, effects):
        qs = Category.objects.get(path=route).products.filter(enable=True)
        if (colors):
            colors_list = list(map(str.strip, colors.split(',')))
            colors_filter = (
                Q(colors__name__in=colors_list)
            )
            qs = qs.filter(colors_filter)

        effects_list = list(map(str.strip, effects.split(',')))

        effect_glow_in_the_dark = 'Светится в темноте' in effects_list
        effect_glow_in_the_uv = 'Светится в ультрафиолете' in effects_list

        effects_filter = Q()
        if effect_glow_in_the_dark:
            effects_filter = effects_filter & Q(glow_in_the_dark=True)
        if effect_glow_in_the_uv:
            effects_filter = effects_filter & Q(glow_in_the_uv=True)
        qs = qs.filter(effects_filter)
        return qs.count()


class Mutations(AuthMutations, graphene.ObjectType):
    pass


class Query(MyQuery, AuthQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
