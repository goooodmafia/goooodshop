from django.db.models import Q, F, Count, Value, BooleanField, CharField

import graphene
from graphene_django_extras import DjangoFilterListField, DjangoFilterPaginateListField, LimitOffsetGraphqlPagination, \
    DjangoListObjectField

from content.models import Content
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

    fetchproducts = DjangoFilterPaginateListField(
        ProductType,
        pagination=LimitOffsetGraphqlPagination(),
        filterset_class=ProductFilter
    )

    fetchproductscount = graphene.Int(
        route=graphene.Argument(graphene.String),
        colors=graphene.Argument(graphene.String),
        effects=graphene.Argument(graphene.String)
    )

    # filters = graphene.Field(FilterType, path=graphene.Argument(graphene.String))
    filters = graphene.List(
        FiltersType,
        route=graphene.Argument(graphene.String),
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

    def resolve_filters(self, info, route, colors, effects):

        # qs = Category.objects.filter(path=route)

        # color_qs = qs.annotate(lable=F('products__colors__name')).values('lable') \
        #     .exclude(lable__isnull=True) \
        #     .annotate(count=Count('lable')) \
        #     .annotate(value=Value(False, output_field=BooleanField())) \
        #     .order_by('lable')

        colors_list = list(filter(None,map(str.strip, colors.split(','))))
        effects_list = list(filter(None,map(str.strip, effects.split(','))))

        effect_glow_in_the_dark = 'Светится в темноте' in effects_list
        effect_glow_in_the_uv = 'Светится в ультрафиолете' in effects_list

        colors_filter = Q()
        print(colors_list)
        if len(colors_list)>0:
            colors_filter = colors_filter & Q(colors__name__in=colors_list)
        # colors_filter =  Q(colors__name__in=colors_list)

        effects_filter = Q()
        if effect_glow_in_the_dark:
            effects_filter = effects_filter & Q(glow_in_the_dark=True)
        if effect_glow_in_the_uv:
            effects_filter = effects_filter & Q(glow_in_the_uv=True)


        products_qs = Product.objects.filter(categories__path=route)
        color_qs = products_qs \
            .annotate(lable=F('colors__name')).values('lable') \
            .exclude(lable__isnull=True) \
            .annotate(count=Count('lable', filter=effects_filter)) \
            .annotate(value=Value(False, output_field=BooleanField())) \
            .order_by('lable')

        # if (colors):
        #     colors_list = list(map(str.strip, colors.split(',')))
        #     colors_filter = (
        #         Q(colors__name__in=colors_list)
        #     )
        #     products_qs = products_qs.filter(colors_filter)

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

        # effects_dark_qs = qs.values('products__glow_in_the_dark') \
        #     .exclude(products__glow_in_the_dark__isnull=True) \
        #     .annotate(count=Count('products__glow_in_the_dark', filter=Q(products__glow_in_the_dark=True))) \
        #     .annotate(lable=Value('Светится в темноте', output_field=CharField())) \
        #     # .values('lable', 'count')
        #
        # effects_uv_qs = qs.values('products__glow_in_the_uv') \
        #     .exclude(products__glow_in_the_uv__isnull=True) \
        #     .annotate(count=Count('products__glow_in_the_uv'), filter=Q(products__glow_in_the_uv=True)) \
        #     .annotate(lable=Value('Светится в ультрафиолете', output_field=CharField())) \
        #     # .values('lable', 'count')

        colors = list(color_qs)

        for color in colors:
            if color['lable'] in colors_list:
                color['value'] = True

        return [
            FiltersType(title='Цвет', name='color', items=colors),
            FiltersType(title='Спецэффекты', name='effects', items=list(products_dark_qs) + list(products_uv_qs)),
            # FiltersType(title='Спецэффекты', name='effects', items=list(effects_dark_qs)+ list(effects_uv_qs)),
            # FiltersType(title='Фильтр', name='filter', items=[]),
        ]


    def resolve_fetchproductscount(self, info, route, colors, effects):
        # return Category.objects.filter(path=route) \
        #     .annotate(num_products=Count('products'))[0].num_products
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

# schema = graphene.Schema(query=Query, mutation=Mutations)
schema = graphene.Schema(query=Query, mutation=Mutations)
