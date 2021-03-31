import tablib
from import_export import resources
from import_export import widgets
from import_export.fields import Field

from shop.models import Product, Tag, Brand, Category, Color, MediaFile
from shop.import_export.widgets import MyGetForeignKeyWidget, MyGetManyToManyWidget, \
    MyCategoriesWidget

from django.utils.text import slugify

import os

from pathlib import Path

from django.conf import settings


def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]


def get_images(brand, sku):
    static_dir = (settings.BASE_DIR / 'static' ).resolve()
    path = static_dir / 'img' / 'products' / brand / sku
    files = []

    print(path)

    for x in path.glob('**/*.jpg'):
        print('\t |- %s' % x)
        if x.is_file():


            f = remove_prefix(str(x), str(static_dir))
            f = '/static%s' % f
            # '/img/products/%s/%s/%s.jpg' % (brand, sku, sku)
            # if (f is not ('/img/products/%s/%s/%s.jpg' % (brand, sku, sku))
                # pass

            print('\t |- - %s' % f)
            #
            if f != ('/static/img/products/%s/%s/%s.jpg' % (brand, sku, sku)):
                files.append(f)
                print('\t |- + %s' % f)
        # [ for x in path.glob('**/*.jpg') if x.is_file()]
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


class ProductResource(VerboseNameModelResource):
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

    def skip_row(self, instance, original):
        if instance.total_count is None:
            skip = True
        else:
            # if instance.total_count > 0:
            #     skip = False
            # else:
            #     skip = True
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

        return instance

    def after_save_instance(self, instance, using_transactions, dry_run):
        # instance.save()

        imgs = get_images(slugify(instance.brand.name), instance.sku)

        for img in imgs:
            (media_file, success) = MediaFile.objects.get_or_create(link=img)
            if (success):
                instance.media_files.add(media_file)

        (tag, success) = Tag.objects.get_or_create(name=instance.model)

        instance.tags.add(tag)
        # if (success):
        #     tag.products.add(instance)

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
            'Мелкий опт от 10шт.',
            'Комиссия, р',
            'Опт. от 15000р',
            '- 3% от 30000р',
            '- 7% от 70000р',
            '- 11% от 110000р',
            '',
            'Кол-во',
            '*',
            '',
            '',
            'XS (42)',
            'S (44)',
            'M (46)',
            'L (48)',
            'XL (50)',
            'XXL (52)',
            'XXХL (54)',
            '4ХL (56)'
        )

    class Meta:
        model = Product
        skip_unchanged = False
        report_skipped = True
        import_id_fields = ('sku',)
        exclude = ('id',)

        fields = ('sku', 'model', 'content', 'brand', 'categories')
        export_order = fields

    # def import_data(self, dataset, *args, **kwargs):
    #
    #     print(dataset)
    #
    #     # del dataset[0:7]
    #
    #     super(ProductResource, self).import_data(dataset, *args, **kwargs)
