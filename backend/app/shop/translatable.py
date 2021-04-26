def myresolver(instance, _info, language_code):
    return instance.safe_translation_getter(_info.field_name, language_code=language_code)