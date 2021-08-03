from django.core.exceptions import ObjectDoesNotExist
from import_export.widgets import ForeignKeyWidget, Widget, ManyToManyWidget, CharWidget

from shop.models import Category, Product
from import_export.fields import Field
from django.conf import settings


class TranslatableField(Field):

    def save(self, obj, data, is_m2m=False):
        """
        If this field is not declared readonly, the object's attribute will
        be set to the value returned by :meth:`~import_export.fields.Field.clean`.
        """
        if not self.readonly:
            attrs = self.attribute.split('__')
            for attr in attrs[:-1]:
                obj = getattr(obj, attr, None)
            cleaned = self.clean(data)

            if cleaned is not None or self.saves_null_values:
                for loc in settings.PARLER_LANGUAGES[None]:
                    obj.set_current_language(loc['code'])
                    if loc['code'] in cleaned:
                        setattr(obj, attrs[-1], cleaned[loc['code']])
                    # else:
                    #     setattr(obj, attrs[-1], '')


class MyModelWidget(Widget):

    def clean(self, value, row=None, *args, **kwargs):
        return value.split('\n')[0]

    def render(self, value, obj=None):
        return value


class MyTagWidget(ManyToManyWidget):

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return self.model.objects.none()
        if isinstance(value, (float, int)):
            ids = [int(value)]
        else:
            ids = value.split(self.separator)[1:]
            ids = filter(None, [i.strip(' ()') for i in ids])

        ids = list(ids)

        for i in ids:
            self.model.objects.get_or_create(**{self.field: i})

        return self.model.objects.filter(**{
            '%s__in' % self.field: ids
        })


from shop.models import SexChoise


class MySexWidget(Widget):
    separator = ';'

    def render(self, value, obj=None):
        return SexChoise.MALE

    def clean(self, value, row=None, *args, **kwargs):
        if value == "":
            return SexChoise.MALE

        s_list = value.split(self.separator)
        s_list = list(filter(None, [i.strip() for i in s_list]))
        if len(s_list) > 1:
            return SexChoise.UNISEX

        return {
            'Мужское': SexChoise.MALE,
            'Женское': SexChoise.FEMALE,
            'Детское': SexChoise.KIDS,
        }.get(s_list[0], SexChoise.MALE)


class MyBooleanWidget(Widget):
    TRUE_VALUE = 'Y'
    FALSE_VALUE = 'N'

    def render(self, value, obj=None):
        if value is None:
            return ""
        return self.TRUE_VALUE if value else self.FALSE_VALUE

    def clean(self, value, row=None, *args, **kwargs):
        if value == "":
            return None
        return True if value in self.TRUE_VALUE else False


class MyGetForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        # val = super().clean(value)
        val = value
        if val:
            obj, created = self.model.objects.get_or_create(**{self.field: val})
            return obj

        else:
            return None


class MyCategoriesWidget(ManyToManyWidget):

    def my_get_or_create(self, name, parent):
        try:
            c = Category.objects.translated('ru', name=name).get(parent=parent)
        except ObjectDoesNotExist:
            c = Category.objects.language('ru').create(name=name, parent=parent)
        return c

    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return self.model.objects.none()

        children = value.split(self.separator)
        parents = row['Описание'].split(self.separator)

        r = []

        for parent in parents:
            for child in children:
                r.append(
                    self.my_get_or_create(
                        name=child.strip(),
                        parent=self.my_get_or_create(name=parent.strip(), parent=None)
                    )
                )

        # print(r)

        return r

        # for i in ids:
        #     self.model.objects.get_or_create(**{self.field: i})

        # return self.model.objects.filter(**{
        #     '%s__in' % self.field: ids
        # })


class MyGetManyToManyWidget(ManyToManyWidget):

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


class MyDescriptionWidget(Widget):
    def render(self, value, obj=None):
        return {
            'ru': obj.safe_translation_getter('description', language_code='ru'),
            'en': obj.safe_translation_getter('description', language_code='en')
        }

    def clean(self, value, row=None, *args, **kwargs):
        return {'ru': value, 'en': row['EN: Описание']}

class MyContentWidget(Widget):
    def render(self, value, obj=None):
        print('321')
        return {
            'ru': obj.safe_translation_getter('content', language_code='ru'),
            'en': obj.safe_translation_getter('content', language_code='en')
        }

    def clean(self, value, row=None, *args, **kwargs):
        print('123')
        return {'ru': value, 'en': row['EN: Описание']}

    # def clean(self, value, row=None, *args, **kwargs):
    #     print('123')
    #     print(row)
    #     return {'ru': row['Состав'], 'en': row['EN: Состав']}