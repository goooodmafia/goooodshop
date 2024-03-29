import tablib
from import_export import resources
from import_export import widgets
from import_export.fields import Field

from shop.models import Product, Tag, Brand, Category, Color, MediaFile
from shop.import_export.widgets import MyGetForeignKeyWidget, MyGetManyToManyWidget, \
    MyCategoriesWidget, MySexWidget, TranslatableField, MyDescriptionWidget, MyContentWidget, MyJSONWidget, \
    MyOrderWidget

from django.utils.text import slugify

import os

from pathlib import Path

from django.conf import settings


def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]


def get_images(brand, sku):
    static_dir = (settings.BASE_DIR / 'static').resolve()
    path = static_dir / 'img' / 'products' / brand / sku
    files = []
    # print(path)
    for x in path.glob('**/*.jpg'):
        # print('\t |- %s' % x)
        if x.is_file():
            f = remove_prefix(str(x), str(static_dir))
            f = '/static%s' % f
            # print('\t |- - %s' % f)
            if f != ('/static/img/products/%s/%s/%s.jpg' % (brand, sku, sku)):
                files.append(f)
                # print('\t |- + %s' % f)
    return files


class VerboseNameModelResource(resources.ModelResource):

    def get_instance(self, instance_loader, row):
        import_id_fields = [
            self.fields[f] for f in self.get_import_id_fields()
        ]
        for field in import_id_fields:
            if field.column_name not in row:
                return
        return instance_loader.get_instance(row)

    @classmethod
    def field_from_django_field(cls, field_name, django_field, readonly):
        """
        Returns a Resource Field instance for the given Django model field.
        """
        FieldWidget = cls.widget_from_django_field(django_field)
        widget_kwargs = cls.widget_kwargs_for_field(field_name)
        field = cls.DEFAULT_RESOURCE_FIELD(
            attribute=field_name,
            column_name=django_field.verbose_name,
            widget=FieldWidget(**widget_kwargs),
            readonly=readonly,
            default=django_field.default,
        )
        return field


class ProductResourceMain(VerboseNameModelResource):

    sku = Field(
        attribute='sku',
        column_name='Артикул',
        widget=widgets.CharWidget()
    )

    model = Field(
        attribute='model',
        column_name='Модель / Цвет',
        # widget=MyModelWidget()
        widget=widgets.CharWidget()
    )

    # tags = Field(
    #     attribute='tags',
    #     column_name = 'Модель / Цвет',
    #     widget=widgets.CharWidget()
    # )

    content = Field(
        attribute='content',
        column_name='Состав',
        widget=widgets.CharWidget()
    )

    brand = Field(
        attribute='brand',
        column_name='Бренд',
        widget=MyGetForeignKeyWidget(model=Brand, field='name')
    )

    categories = Field(
        attribute='categories',
        column_name='Доп. параметры',
        widget=MyCategoriesWidget(model=Category, field='name', separator=';')
    )

    colors = Field(
        attribute='colors',
        column_name='Цвет',
        widget=MyGetManyToManyWidget(model=Color, field='name', separator=';')
    )

    total_count = Field(
        attribute='total_count',
        column_name='Кол-во',
        widget=widgets.IntegerWidget()
    )

    sex = Field(
        attribute='sex',
        column_name='Описание',
        widget=MySexWidget()
    )

    price_ret = Field(default=0, attribute='price_ret', column_name='Розничная цена, р',
                      widget=widgets.IntegerWidget())
    price_ret_sale = Field(default=0, attribute='price_ret_sale', column_name='Розничная цена, с учетом скидки, р',
                           widget=widgets.IntegerWidget())
    price_opt_m = Field(default=0, attribute='price_opt_m', column_name='Мелкий опт от 10шт.',
                        widget=widgets.IntegerWidget())
    price_opt_1 = Field(default=0, attribute='price_opt_1', column_name='Опт. от 15000р',
                        widget=widgets.IntegerWidget())
    price_opt_2 = Field(default=0, attribute='price_opt_2', column_name='- 3% от 30000р',
                        widget=widgets.IntegerWidget())
    price_opt_3 = Field(default=0, attribute='price_opt_3', column_name='- 7% от 70000р',
                        widget=widgets.IntegerWidget())
    price_opt_4 = Field(default=0, attribute='price_opt_4', column_name='- 11% от 110000р',
                        widget=widgets.IntegerWidget())

    size_ns = Field(default=0, attribute='size_ns', column_name='NO SIZE', widget=widgets.IntegerWidget())

    size_3xs = Field(default=0, attribute='size_xxxs', column_name='XXXS', widget=widgets.IntegerWidget())
    size_2xs = Field(default=0, attribute='size_xxs', column_name='XXS', widget=widgets.IntegerWidget())
    size_xs = Field(default=0, attribute='size_xs', column_name='XS (42)', widget=widgets.IntegerWidget())
    size_s = Field(default=0, attribute='size_s', column_name='S (44)', widget=widgets.IntegerWidget())
    size_m = Field(default=0, attribute='size_m', column_name='M (46)', widget=widgets.IntegerWidget())
    size_l = Field(default=0, attribute='size_l', column_name='L (48)', widget=widgets.IntegerWidget())
    size_xl = Field(default=0, attribute='size_xl', column_name='XL (50)', widget=widgets.IntegerWidget())
    size_2xl = Field(default=0, attribute='size_2xl', column_name='XXL (52)', widget=widgets.IntegerWidget())
    size_3xl = Field(default=0, attribute='size_3xl', column_name='XXХL (54-56)', widget=widgets.IntegerWidget())
    size_4xl = Field(default=0, attribute='size_4xl', column_name='4ХL (58)', widget=widgets.IntegerWidget())

    def skip_row(self, instance, original):
        if instance.total_count is None:
            skip = True
        else:
            skip = False

        return skip

    def get_img(self, sku, brand):
        return '/static/img/products/%s/%s/%s.jpg' % (brand, sku, sku)

    def before_save_instance(self, instance, using_transactions, dry_run):
        def switcher(argument):
            return {
                '(Светится в темноте и ультрафиолете)': (False, False, False, True, True),
                '(Светится в ультрафиолете)': (False, False, False, False, True),
                '(Светится в темноте)': (False, False, False, True, False),
                'SALE!': (False, False, True, False, False),
                'ХИТ!': (True, False, False, False, False),
                'NEW!': (False, True, False, False, False),
            }.get(argument, (False, False, False, False, False))

        temp = instance.model.split('\n')

        result_list = []
        instance.model = temp[0]

        for item in temp:
            result_list.append(switcher(item))

        (instance.hit,
         instance.new,
         instance.sale,
         instance.glow_in_th_dark,
         instance.glow_in_th_uv) = map(any, zip(*result_list))

        instance.thumbnail = MediaFile.objects.get_or_create(
            link=self.get_img(
                instance.sku,
                slugify(instance.brand.name)
            )
        )[0]

        # instance.my_order = self.order
        # self.order += 1

        return instance

    def after_save_instance(self, instance, using_transactions, dry_run):

        imgs = get_images(slugify(instance.brand.name), instance.sku)

        for img in imgs:
            (media_file, success) = MediaFile.objects.get_or_create(link=img)
            if (success):
                instance.media_files.add(media_file)

        # (tag, success) = Tag.objects.get_or_create(name=instance.model)
        #
        # instance.tags.add(tag)

        return instance

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        del dataset[0:8]
        dataset.headers = (
            'Артикул',
            'Превью',
            'Модель / Цвет',
            'Раздел',
            'Бренд',
            'Описание',
            'Доп. параметры',
            'Цвет',
            'Состав',
            'Розничная цена, р',
            'Розничная цена, с учетом скидки, р',
            'Мелкий опт от 10шт.',
            'Комиссия, р',
            'Опт. от 15000р',
            '- 3% от 30000р',
            '- 7% от 70000р',
            '- 11% от 110000р',
            '',
            'Кол-во',
            'NO SIZE',
            'XXXS',
            'XXS',
            'XS (42)',
            'S (44)',
            'M (46)',
            'L (48)',
            'XL (50)',
            'XXL (52)',
            'XXХL (54-56)',
            '4ХL (58)',
            '5XL(62)'
        )

    class Meta:
        model = Product
        skip_unchanged = False
        report_skipped = True
        import_id_fields = ('sku',)
        exclude = ('id',)

        fields = ('sku', 'model', 'content', 'brand', 'categories')
        export_order = fields


class ProductResourceSecondary(VerboseNameModelResource):
    sku = Field(
        attribute='sku',
        column_name='Артикул',
        widget=widgets.CharWidget()
    )

    # description = TranslatableField(
    #     attribute='description',
    #     column_name='Описание',
    #     widget=MyDescriptionWidget()
    # )

    content = TranslatableField(
        attribute='content',
        column_name='EN: Состав',
        widget=MyContentWidget(),
        # widget=widgets.JSONWidget()
        # readonly=False,
        saves_null_values=False
    )

    tags = Field(
        attribute='tags',
        column_name='Тематика Дизайна',

        widget=MyGetManyToManyWidget(
            model=Tag,
            field="name",
            separator=';'
        )
    )
    tags_en = Field(
        attribute='tags_en',
        column_name='EN: Тематика Дизайна',

        widget=MyGetManyToManyWidget(
            model=Tag,
            field="name",
            separator=';'
        )
    )

    colors_en = Field(
        attribute='colors_en',
        column_name='EN: Цвет',
        widget=MyGetManyToManyWidget(model=Color, field='name', separator=';')
    )

    my_order = Field(
        attribute='my_order',
        column_name='Порядок в каталоге',
        widget=MyOrderWidget()
    )

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        del dataset[0:8]
        dataset.headers = (
            'Артикул',
            'Превью',
            'Модель / Цвет',
            '',
            '',
            'Описание',
            'Тематика Дизайна',
            'Пол',
            'Правила ухода',
            'Страна производитель',
            'Дата и время добавления',
            'Порядок в каталоге',
            'Наличие ',
            'NO SIZE Параметры размера',
            'XXXS Параметры размера',
            'XXS Параметры размера',
            'XS Параметры размера',
            'S Параметры размера',
            'M Параметры размера в сантиметрах',
            'L Параметры размера',
            'XL Параметры размера',
            'XXL Параметры размера',
            '3XL Параметры размера',
            '4XL Параметры размера',
            '5XL Параметры размера',
            'EN: Модель (Название Дизайна)',
            'EN: Бренд',
            'EN: Описание',
            'EN: Цвет',
            'EN: Тематика Дизайна',
            'EN: Верхняя категория товара',
            'EN: Категории товара',
            'EN: Состав',
            'EN: Пол',
            'EN: Правила ухода',
            'EN: Страна производитель',
            'EN: Розничная цена, $',
            'EN: Цена Мелкий Опт, $',
            'EN: Цена Опт-1, $',
            'EN: Цена Опт-2, $',
            'EN: Цена Опт-3, $',
            'EN: Цена Опт-4, $',
            'EN: Спецэффект',
            'EN: NO SIZE Параметры размера',
            'EN: XXXS Параметры размера',
            'EN: XXS Параметры размера',
            'EN: XS Параметры размера',
            'EN: S Параметры размера',
            'EN: M Параметры размера',
            'EN: L Параметры размера',
            'EN: XL Параметры размера',
            'EN: XXL Параметры размера',
            'EN: 3XL Параметры размера',
            'EN: 4XL Параметры размера',
            'EN: 5XL Параметры размера',
        )

    def skip_row(self, instance, original):
        return not Product.objects.filter(sku=instance.sku).exists()

    class Meta:
        model = Product
        skip_unchanged = False
        report_skipped = True
        import_id_fields = ('sku',)
        exclude = ('id', 'total_count')

        fields = (
            'sku',
            # 'description',
            'content'
        )
        export_order = fields
