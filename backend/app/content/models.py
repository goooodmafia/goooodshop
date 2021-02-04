from django.db import models

# Create your models here.
from parler.models import TranslatedFields, TranslatableModel

CONTENT_POSITIONS = [
    ('HEADER_TOP', 'Над заголовком'),
    ('HEADER_BOTTOM', 'Под заголовком'),
    ('DEFAULT_TOP', 'Выше контента'),
    ('DEFAULT_BOTTOM', 'Ниже контета'),
    ('FOOTER_TOP', 'Над подвалом'),
    ('FOOTER_BOTTOM', 'Под подвалом'),
]


class Content(TranslatableModel):
    title = models.CharField(max_length=256, blank=False, verbose_name='Заголовок')
    route = models.CharField(max_length=256, blank=False, verbose_name='Путь')
    position = models.CharField(max_length=32,choices=CONTENT_POSITIONS, default='DEFAULT_TOP', verbose_name='позиция')

    translations = TranslatedFields(
        data=models.TextField()
    )

    enable = models.BooleanField(default=True, verbose_name='Показывать')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)


    def __str__(self):
        return '%s (%s)' % (self.title, self.get_position_display())