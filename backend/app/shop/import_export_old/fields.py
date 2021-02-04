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
                for loc in settings.PARLER_LANGUAGES[1]:
                    obj.set_current_language(loc['code'])
                    if loc['code'] in cleaned:
                        setattr(obj, attrs[-1], cleaned[loc['code']])
                    else:
                        setattr(obj, attrs[-1], '')
                        # if obj.has_translation(language_code=loc['code'], related_name=attrs[-1]):
                        #     pass
                            # obj.delete_translation(language_code=loc['code'], related_name=attrs[-1])
