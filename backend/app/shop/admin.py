from django.contrib import admin
from django.contrib.admin import register
from django.urls import path
from import_export.admin import ImportExportModelAdmin, ExportMixin, ImportMixin

from mptt.admin import MPTTModelAdmin
from mptt.forms import MPTTAdminForm
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm

from shop.import_export.MyImportMixin import MyImportMixin
from shop.models import Product, Category, Brand, MediaFile, Tag, Color
from shop.import_export.resources import ProductResourceMain, ProductResourceSecondary

from adminsortable2.admin import SortableAdminMixin


# class ImportExportMixinAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
#
#     def get_import_formats(self):
#         formats = (
#             base_formats.XLS,
#         )
#         return [f for f in formats if f().can_import()]
#
#     def get_export_formats(self):
#         formats = (
#             base_formats.XLS,
#         )
#         return [f for f in formats if f().can_export()]
#
#     class Meta:
#         abstract = True


class MyImportMixinAdmin(MyImportMixin, admin.ModelAdmin):
    resource_class_first = ProductResourceMain
    resource_class_second = ProductResourceSecondary

    class Meta:
        abstract = True
#
# class MyImportMixinAdminSecondary(ImportMixin, admin.ModelAdmin):
#     change_list_template = 'shop/admin/import_export/change_list_import.html'
#     resource_class = ProductResourceSecondary
#
#     def get_urls(self):
#         urls = super().get_urls()
#         info = self.get_model_info()
#         my_urls = [
#             path('process_import/',
#                  self.admin_site.admin_view(self.process_import),
#                  name='%s_%s_process_import' % info),
#             path('import_secondary/',
#                  self.admin_site.admin_view(self.import_action),
#                  name='%s_%s_import_secondary' % info),
#         ]
#         return my_urls + urls
#
#     class Meta:
#         abstract = True

# class ImportMixinAdminSecondary(SecondaryImportMixin, admin.ModelAdmin):
#     resource_class = ProductResourceSecondary
#     class Meta:
#         abstract = True

# class MyImportExportMixinAdminSecondary(ImportMixin, admin.ModelAdmin):
#     resource_class = ProductResourceSecondary
#     class Meta:
#         abstract = True

class CategoryAdminForm(MPTTAdminForm, TranslatableModelForm):
    pass


@register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    search_fields = ['link']


# @register(Price)
# class PriceAdmin(admin.ModelAdmin):
#     pass

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
# class ProductAdmin(TranslatableAdmin,ImportExportModelAdmin, ImportExportMixinAdmin):
class ProductAdmin(TranslatableAdmin,
                   # ImportMixin,
                   MyImportMixinAdmin,
                   # ImportMixinAdminMain,
                   # MyImportMixinAdminSecondary,
                   # MyImportExportMixinAdminSecondary,

                   SortableAdminMixin):
    # resource_class = ProductResourceMain
    readonly_fields = ['pub_date', 'mod_date']
    # autocomplete_fields = ['media_files','video_files', 'thumbnail', 'categories']
    list_display = (
        # 'my_order',
        'sku',
        'model',

        'description',
        'get_categories',
        'get_tags',
        'get_colors',
        'enable',
        # 'price',
        'pub_date',
        'mod_date'
    )

    # filter_horizontal = ('tags', 'categories', 'colors', 'media_files',)
    filter_horizontal = ('media_files',)

    autocomplete_fields = ['thumbnail', 'tags', 'categories', 'colors']

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

    fieldsets = (
        (None, {
            'fields': (
                'sku',
                'model',
                'slug',
                'brand',
                # 'price',
                'description',
                'content',
                'categories',
                'tags',
                'colors',
                'thumbnail',
                'sex',
                'media_files',
                'price_ret',
                'price_ret_sale',
                'price_opt_m',
                'price_opt_1',
                'price_opt_2',
                'price_opt_3',
                'price_opt_4',
                'total_count',
                'size_ns',
                'size_3xs',
                'size_2xs',
                'size_xs',
                'size_s',
                'size_m',
                'size_l',
                'size_xl',
                'size_2xl',
                'size_3xl',
                'size_4xl',
                'size_5xl',
                'size_6xl',
                'new',
                'hit',
                'sale',
                'glow_in_the_dark',
                'glow_in_the_uv',
                'enable',

                'pub_date',
                'mod_date',
            ),
        }),
    )

    class Meta:
        ordering = ['my_order']


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


@register(Color)
class ColorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)
