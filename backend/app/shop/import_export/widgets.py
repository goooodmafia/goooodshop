from django.core.exceptions import ObjectDoesNotExist
from import_export.widgets import ForeignKeyWidget, Widget, ManyToManyWidget

from shop.models import Category


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
            c = Category.objects.language('ru').create(name=name,parent=parent)
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
                        name=child,
                        parent=self.my_get_or_create(name=parent, parent=None)
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
