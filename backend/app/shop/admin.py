from django.contrib import admin
from django.contrib.admin import register
from import_export.admin import ImportExportModelAdmin, ExportMixin, ImportMixin
from import_export.formats import base_formats
from mptt.admin import MPTTModelAdmin
from mptt.forms import MPTTAdminForm
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm

from shop.models import Product, Category, Brand, MediaFile, Tag, Color
from shop.import_export.resources import ProductResource


class ImportExportMixinAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):

    def get_import_formats(self):
        formats = (
            base_formats.XLS,
        )
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]

    class Meta:
        abstract = True


class CategoryAdminForm(MPTTAdminForm, TranslatableModelForm):
    pass


@register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    search_fields = ['link']


class ProductInline(admin.TabularInline):
    # class ProductInline(admin.StackedInline):
    model = Category.products.through
    extra = 0


@register(Category)
class CategoryAdmin(TranslatableAdmin, MPTTModelAdmin):
    form = CategoryAdminForm

    search_fields = ['full_name']
    ordering = ['full_name']

    inlines = [
        ProductInline,
    ]

    readonly_fields = ['pub_date', 'mod_date', 'path', 'full_name', ]

    list_display = ('full_name', 'slug', 'path')
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'parent', 'path', 'full_name', 'description', 'pub_date', 'mod_date'),
        }),
    )


# class TagInline(admin.TabularInline):
#     model = Tag

@register(Product)
class ProductAdmin(TranslatableAdmin, ImportExportModelAdmin, ImportExportMixinAdmin):
    resource_class = ProductResource
    readonly_fields = ['pub_date', 'mod_date']
    # autocomplete_fields = ['media_files','video_files', 'thumbnail', 'categories']
    list_display = (
        'sku',
        'model',

        'description',
        'get_categories',
        'get_tags',
        'get_colors',
        'enable',
        'price',
        'pub_date',
        'mod_date'
    )

    # filter_horizontal = ('tags', 'categories', 'colors')

    autocomplete_fields = ['thumbnail', 'media_files', 'tags', 'categories', 'colors']

    def get_categories(self, obj):
        return " | ".join([c.full_name for c in obj.categories.all()])

    def get_tags(self, obj):
        return " | ".join([c.name for c in obj.tags.all()])

    def get_colors(self, obj):
        return " | ".join([c.name for c in obj.colors.all()])

    get_categories.short_description = 'Категории'
    get_tags.short_description = 'Теги'
    get_colors.short_description = 'Цвет'

    search_fields = ['sku', 'model', 'tags__name', 'colors__name', 'categories__full_name']
    list_filter = ['brand', 'enable', 'colors', 'tags']


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@register(Color)
class ColorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
