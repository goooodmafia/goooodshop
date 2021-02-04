from django.contrib import admin

# Register your models here.
from django.contrib.admin import register
from django.db import models
from parler.admin import TranslatableAdmin

from content.models import Content
from pagedown.widgets import AdminPagedownWidget

@register(Content)
class ContentAdmin(TranslatableAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    readonly_fields = ['pub_date', 'mod_date']

    list_display = ('title', 'route', 'position', 'pub_date', 'mod_date')

    list_filter = ['route', 'position']
    search_fields = ['title']
    ordering = ['-mod_date']