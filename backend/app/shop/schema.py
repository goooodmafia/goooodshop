import graphene
from django.db.models import Q, Count
import django_filters
from django_parler_graphql.fields import TranslatedInstanceFields
from graphene.types.generic import GenericScalar

import graphene_django
from graphene_django_extras import DjangoObjectType, DjangoListObjectType, LimitOffsetGraphqlPagination, \
    DjangoListObjectField
from shop.translatable import myresolver
from shop.models import Category, Product, MediaFile, Tag


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
    colors = django_filters.CharFilter(method='my_colors_filter')
    tags = django_filters.CharFilter(method='my_tags_filter')
    route = django_filters.CharFilter(method='my_path_filter')
    effects = django_filters.CharFilter(method='my_effects_filter')

    def my_query_filter(self, queryset, name, value):
        query_filter = (
                Q(translations__description__icontains=value) |
                Q(model__icontains=value) |
                Q(sku__icontains=value)
        )
        return queryset.filter(query_filter)

    def my_colors_filter(self, queryset, name, value):
        colors = list(map(str.strip, value.split(',')))
        query_filter = (
            Q(colors__name__in=colors)
        )
        return queryset.filter(query_filter)

    def my_tags_filter(self, queryset, name, value):
        tags = list(map(str.strip, value.split(',')))
        query_filter = (
            Q(tags__name__in=tags)
        )
        return queryset.filter(query_filter)

    def my_path_filter(self, queryset, name, value):

        query_filter = (
            Q(categories__path__iexact=value)
        )
        return queryset.filter(query_filter)

    def my_effects_filter(self, queryset, name, value):

        effects_list = list(map(str.strip, value.split(',')))

        effect_glow_in_the_dark = 'Светится в темноте' in effects_list
        effect_glow_in_the_uv = 'Светится в ультрафиолете' in effects_list

        effects_filter = Q()
        if effect_glow_in_the_dark:
            effects_filter = effects_filter & Q(glow_in_the_dark=True)
        if effect_glow_in_the_uv:
            effects_filter = effects_filter & Q(glow_in_the_uv=True)

        return queryset.filter(effects_filter)

    class Meta:
        model = Product
        fields = {
            "model": ("icontains", "iexact"),
            "sku": ("icontains", "iexact"),
        }


class ProductType(DjangoObjectType):
    description = TranslatedInstanceFields(graphene.String, resolver=myresolver)
    content = TranslatedInstanceFields(graphene.String, resolver=myresolver)
    colors = graphene.List(graphene.String)
    thumbnail = graphene.Field(graphene.String)
    mediaFiles = graphene.List(GenericScalar)
    tags = graphene.List(graphene.String)
    brand = graphene.String()
    category = GenericScalar()

    price = graphene.Field(graphene.Int)
    sizes = graphene.List(GenericScalar)

    breadcrumbs = graphene.List(GenericScalar)

    def resolve_colors(self, info):
        return [color.name for color in self.colors.all()]

    def resolve_tags(self, info):
        return [tag.name for tag in self.tags.all()]

    def resolve_brand(self, info):
        return self.brand.name

    def resolve_category(self, info):
        qs = self.categories.all()[0]
        return {'title': qs.full_name, 'link': qs.path}

    def resolve_mediaFiles(self, info):
        return [{'src': media.link} for media in self.media_files.all()]

    def resolve_thumbnail(self, info):
        return self.thumbnail.link

    def resolve_breadcrumbs(self, info):
        return self.categories.all()[0].breadcrumbs

    def resolve_price(self, info):
        return self.price_ret

    def resolve_sizes(self, info):
        return [
            {'size_ns': self.size_ns},
            {'size_xs': self.size_xs},
            {'size_s': self.size_s},
            {'size_m': self.size_m},
            {'size_l': self.size_l},
            {'size_xl': self.size_xl},
            {'size_2xl': self.size_2xl},
            {'size_3xl': self.size_3xl},
            {'size_4xl': self.size_4xl},
        ]

    class Meta:
        model = Product
        # exclude = (
        #     'price_ret',
        #     'price_opt_m',
        #     'price_opt_1',
        #     'price_opt_2',
        #     'price_opt_3',
        #     'price_opt_4',
        # )

        only_fields = (
            'model',
            'sku',
            'slug',
            'thumbnail',
            'mediaFiles',
            'colors',
            'category',
            'new',
            'hit',
            'sale',
            'glow_in_the_dark',
            'glow_in_the_uv',
            'description',
            'content',
            'price',

            'sizes',

        )


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
        return self.products \
            .filter(total_count__gt=0)

    def resolve_children(self, info):
        return self.children \
            .annotate(num_products=Count('products', Q(products__total_count__gt=0))).filter(num_products__gt=0)

    class Meta:
        model = Category


class FiltersType(graphene.ObjectType):
    title = graphene.String()
    name = graphene.String()
    items = graphene.List(GenericScalar)

# class FilterType(graphene.ObjectType):
#     colors = graphene.List(GenericScalar)

# def resolve_colors(self, info):
#     # print(instance)
#     return 42
