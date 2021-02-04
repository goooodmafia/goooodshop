from django.core.exceptions import ObjectDoesNotExist
from import_export.widgets import Widget, ForeignKeyWidget
from django.conf import settings


# class MyMultiLanguageWidjet(Widget):
#
#     def __init__(self, model, *args, **kwargs):
#         self.model = model
#         super().__init__(*args, **kwargs)
#
#     # def get_queryset(self, value, row):
#     #     return self.model.objects.get(
#     #         sku=row["sku"]
#     #     )
#
#     def clean(self, value, row=None, *args, **kwargs):
#         print(value)
#         # obj = self.get_queryset(value, row, *args, **kwargs)
#         # obj.set_current_language('de')
#         # obj.fi
#
#         return value
#
#     def render(self, value, obj=None):
#         return '|\n'.join(loc for loc in value.get_available_languages())
#
#         # return '|\n'.join(
#         #     '%s:\"%s\"' % (loc['code'], value.safe_translation_getter('description', language_code=loc['code'])) for loc
#         #     in
#         #     settings.PARLER_LANGUAGES[1])


class MyBooleanWidget(Widget):
    """
    Widget for converting boolean fields.
    """
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


class MyForeignKeyWidget(ForeignKeyWidget):

    def clean(self, value, row=None, *args, **kwargs):
        val = super().clean(value)
        if val:
            return self.get_queryset(value, row, *args, **kwargs).get(**{self.field: val})
        else:
            return None

    def render(self, value, obj=None):
        if value is None:
            return ""

        attrs = self.field.split('__')
        for attr in attrs:
            try:
                value = getattr(value, attr, None)
            except (ValueError, ObjectDoesNotExist):
                # needs to have a primary key value before a many-to-many
                # relationship can be used.
                return None
            if value is None:
                return None

        return value