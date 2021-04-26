from django.contrib import admin

# Register your models here.
from django.contrib.admin import register
from parler.admin import TranslatableAdmin

from news.models import News


@register(News)
class NewsAdmin(TranslatableAdmin, admin.ModelAdmin):
    list_display = [
        'title',
        'view_date',
        'pub_date',
        'mod_date'
    ]


    readonly_fields = ['pub_date', 'mod_date']

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'image',
                'link',
                'description',
                'slug',
                'enable',
                'view_date',
                'pub_date',
                'mod_date'
            ),
        }),
    )



