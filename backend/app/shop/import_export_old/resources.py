from import_export import resources
from import_export import widgets
from import_export.fields import Field

from ..models import Product, Brand, Category, MediaFile
from .widgets import MyBooleanWidget
from .fields import TranslatableField

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


class MyGetForeignKeyWidget(widgets.ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        # val = super().clean(value)
        val = value
        if val:
            obj, created = self.model.objects.get_or_create(**{self.field: val})
            return obj

        else:
            return None


class MyGetManyToManyWidget(widgets.ManyToManyWidget):

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return self.model.objects.none()
        if isinstance(value, (float, int)):
            ids = [int(value)]
        else:
            ids = value.split(self.separator)
            ids = filter(None, [i.strip() for i in ids])

        ids = list(ids)

        for i in ids:
            self.model.objects.get_or_create(**{self.field: i})

        return self.model.objects.filter(**{
            '%s__in' % self.field: ids
        })


class ProductResource(VerboseNameModelResource):
    brand = Field(
        attribute='brand',
        column_name='Бренд',
        widget=widgets.ForeignKeyWidget(Brand, field='code')
    )

    enable = Field(
        attribute='enable',
        column_name='Показывать',
        widget=MyBooleanWidget()
    )

    categories = Field(
        attribute='categories',
        column_name='Категории',
        widget=widgets.ManyToManyWidget(Category, field='full_name', separator='\n')
    )

    description = TranslatableField(
        attribute='description',
        column_name="Описание",
        widget=widgets.JSONWidget(),
        saves_null_values=False
    )

    content = TranslatableField(
        attribute='content',
        column_name="Состав",
        widget=widgets.JSONWidget(),
        saves_null_values=False
    )

    thumbnail = Field(
        attribute='thumbnail',
        column_name='Превью',
        # widget=widgets.ForeignKeyWidget(MediaFile, field='link')
        widget=MyGetForeignKeyWidget(MediaFile, field='link')
    )

    media_files = Field(
        attribute='media_files',
        column_name='Медиа файлы',
        # widget=widgets.ManyToManyWidget(MediaFile, field='link', separator='\n')
        widget=MyGetManyToManyWidget(MediaFile, field='link', separator='\n')
    )

    video_files = Field(
        attribute='video_files',
        column_name='Видео',
        # widget=widgets.ManyToManyWidget(MediaFile, field='link', separator='\n')
        widget=MyGetManyToManyWidget(MediaFile, field='link', separator='\n')
    )

    def get_locales(self, product, order=("ru", "en")):
        available_locales = product.get_available_languages(include_unsaved=True)
        export_order = order + tuple(l for l in available_locales if l not in order)
        return [l for l in export_order if l in available_locales]

    def dehydrate_description(self, product):
        return {loc: product.safe_translation_getter('description', language_code=loc) for loc in
                self.get_locales(product)}

    def dehydrate_content(self, product):
        return {loc: product.safe_translation_getter('content', language_code=loc) for loc in self.get_locales(product)}


    class Meta:
        model = Product
        skip_unchanged = False
        report_skipped = True
        import_id_fields = ('sku',)
        exclude = ('id',)
        widgets = {
            'pub_date': {'format': '%d.%m.%y %H:%M'},
            'mod_date': {'format': '%d.%m.%y %H:%M'},
        }

        fields = ('sku',
                  'model',
                  'brand',
                  'enable',
                  'categories',
                  'description',
                  'content',
                  'thumbnail',
                  'media_files',
                  'video_files',
                  'price',
                  )

        export_order = fields