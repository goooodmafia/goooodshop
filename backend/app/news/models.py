from django.db import models

from django.utils import timezone
from parler.models import TranslatableModel
from parler.models import TranslatedFields

from shop.models import MediaFile


class News(TranslatableModel):
    title = models.CharField(max_length=256)

    translations = TranslatedFields(
        description=models.TextField(blank=True, default='', verbose_name='Описание'),
    )

    image = models.OneToOneField(
        MediaFile,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="news_image",
        verbose_name='КДПВ'
    )

    link = models.CharField(max_length=255, blank=True, verbose_name='Ссылка')

    slug = models.SlugField(max_length=256, unique=True, blank=True)
    enable = models.BooleanField(default=True)

    view_date = models.DateTimeField(verbose_name='Дата публикации')

    pub_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    mod_date = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def create_slug(self):
        if self.slug == '':
            self.slug = self.pub_date.strftime("%y%m%d%H%M")

    def save(self, *args, **kwargs):
        if not self.id:
            self.pub_date = timezone.now()
        if not self.view_date:
            self.view_date = timezone.now()
        self.mod_date = timezone.now()
        self.create_slug()
        return super(News, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.title, self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-view_date']
        verbose_name = "новинку"
        verbose_name_plural = "новинки"