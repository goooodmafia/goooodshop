import graphene
from django.db.models import Q, Count
import django_filters
from django_parler_graphql.fields import TranslatedInstanceFields
from graphene.types.generic import GenericScalar

import graphene_django
from graphene_django_extras import DjangoObjectType, DjangoListObjectType, LimitOffsetGraphqlPagination, \
    DjangoListObjectField

from shop.models import Category, Product, MediaFile, Tag


def myresolver(instance, _info, language_code):
    return instance.safe_translation_getter(_info.field_name, language_code=language_code)


class MediaFileType(DjangoObjectType):
    class Meta:
        model = MediaFile
        fields = ('link',)


class TagType(DjangoListObjectType):
    class Meta:
        model = Tag
        fields = ('name',)


class ProductFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='my_query_filter')

    def my_query_filter(self, queryset, name, value):
        query_filter = (
                Q(translations__description__icontains=value) |
                Q(model__icontains=value) |
                Q(sku__icontains=value)
        )
        return queryset.filter(query_filter)

    class Meta:
        model = Product
        fields = {
            "model": ("icontains", "iexact"),
            "sku": ("icontains", "iexact"),
            "categories__path": ("icontains", "iexact"),
        }


class ProductType(DjangoObjectType):
    description = TranslatedInstanceFields(graphene.String, resolver=myresolver)
    content = TranslatedInstanceFields(graphene.String, resolver=myresolver)
    colors = graphene.List(graphene.String)
    thumbnail = graphene.Field(MediaFileType)
    tags = graphene.List(TagType)

    def resolve_colors(self, info):
        return [color.name for color in self.colors.all()]

    class Meta:
        model = Product


class ProductListType(DjangoListObjectType):
    thumbnail = graphene.List(MediaFileType)
    tags = DjangoListObjectField(TagType)

    class Meta:
        model = Product
        pagination = LimitOffsetGraphqlPagination(default_limit=25)


class CategoryType(graphene_django.DjangoObjectType):
    breadcrumbs = graphene.List(GenericScalar)
    name = TranslatedInstanceFields(graphene.String, resolver=myresolver)
    products = graphene.List(ProductType)
    children = graphene.List(lambda: CategoryType)

    def resolve_products(self, info):
        return self.products\
            .filter(total_count__gt=0)

    def resolve_children(self, info):
        return self.children\
            .annotate(num_products=Count('products', Q(products__total_count__gt=0))).filter(num_products__gt=0)


    class Meta:
        model = Category


class FilterType(graphene.ObjectType):
    colors = graphene.List(graphene.String)

    # def resolve_colors(self, info):
    #     # print(instance)
    #     return 42