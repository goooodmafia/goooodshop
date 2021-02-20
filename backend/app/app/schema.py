from django.db.models import Q, F, Count, Value, BooleanField
from graphene_django import DjangoObjectType
import graphene
from graphene_django_extras import DjangoFilterListField, DjangoFilterPaginateListField, LimitOffsetGraphqlPagination, \
    DjangoListObjectField



from content.models import Content
from shop.models import Category, Product
from shop.schema import CategoryType, ProductType, ProductListType, ProductFilter, FilterType, FiltersType
from users.models import CustomUser as UserModel

from content.schema import ContentType
from content.schema import PositionEnum


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    # users = graphene.List(User)
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

    # filters = graphene.Field(FilterType, path=graphene.Argument(graphene.String))
    filters = graphene.List(FiltersType, route=graphene.Argument(graphene.String))

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

    def resolve_filters(self, info, route):

        qs = Category.objects.filter(path=route) \
            .annotate(lable=F('products__colors__name')).values('lable') \
            .exclude(lable__isnull=True) \
            .annotate(count=Count('lable')) \
            .annotate(value=Value(False, output_field=BooleanField())) \
            .order_by('lable')


        return [
            FiltersType(title='Цвет', name='color', items=qs),
            # FiltersType(title='Фильтр', name='filter', items=[]),
            # FiltersType(title='Фильтр', name='filter', items=[]),
        ]

        # qs = Category.objects.filter(path=path) \
        #     .values('products__colors__name').annotate(count=Count('products__colors__name')) \
        #     .order_by('products__colors__name')

        # qs = Category.objects.filter(path=path) \
        #     .annotate(lable = F('products__colors__name')).values('lable')\
        #     .annotate(count=Count('lable')) \
        #     .annotate(value=Value(False, output_field=BooleanField())) \
        #     .order_by('lable')
        #
        # return FilterType(
        #     colors = qs
        # )

        # def resolve_products(self, info, path, query):
        #     qs = Category.objects.get(path=path).products
        #     if query:
        #         print(query)
        #         query_filter = (
        #                 Q(translations__description__icontains=query) |
        #                 Q(model__icontains=query) |
        #                 Q(sku__icontains=query)
        #         )
        #         qs = qs.filter(query_filter)
        #     # if filters:
        #     #     print(filters)
        #     #     qs = qs.filter(**filters)
        #     return qs


schema = graphene.Schema(query=Query)
