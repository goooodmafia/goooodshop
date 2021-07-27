from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from mptt.models import MPTTModel
from parler.models import TranslatableModel, TranslatedFields, TranslatableModelMixin
from unidecode import unidecode

from .managers import CategoryManager


class MediaFile(models.Model):
    link = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'медиа файлы'
        verbose_name_plural = 'медиа файлы'

    def __str__(self):
        return self.link


class Brand(models.Model):
    name = models.CharField(blank=False, default='', max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'


# class Price(models.Model):
#     price_ret = models.IntegerField(blank=False, default=0, verbose_name='Розничная цена')
#     price_opt_m = models.IntegerField(blank=False, default=0, verbose_name='Мелкий Опт')
#     price_opt_1 = models.IntegerField(blank=False, default=0, verbose_name='Опт от 11000')
#     price_opt_2 = models.IntegerField(blank=False, default=0, verbose_name='Опт от 30000')
#     price_opt_3 = models.IntegerField(blank=False, default=0, verbose_name='Опт от 70000')
#     price_opt_4 = models.IntegerField(blank=False, default=0, verbose_name='Опт от 110000')
#
#     mod_date = models.DateTimeField(auto_now=True, verbose_name='Изменен')
#     class Meta:
#         verbose_name = 'Цена'
#         verbose_name_plural = 'Цены'


class Category(MPTTModel, TranslatableModel):
    parent = models.ForeignKey(
        'self',
        null=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name='Родительская категория'
    )
    translations = TranslatedFields(
        description=models.TextField(blank=True, default='', verbose_name='Описание'),
        content=models.TextField(blank=True, default='', verbose_name='Состав'),
        name=models.CharField(max_length=1024, blank=True, verbose_name='Имя')
    )
    full_name = models.CharField(max_length=1024, blank=True, verbose_name='Полное имя')
    path = models.CharField(max_length=256, blank=True, unique=True, verbose_name='Путь')

    enable = models.BooleanField(default=True, verbose_name='Показывать')
    slug = models.SlugField(max_length=128, blank=True, verbose_name='ЧПУ ссылка')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    mod_date = models.DateTimeField(auto_now=True, verbose_name='Изменен')

    objects = CategoryManager()

    @property
    def breadcrumbs(self):
        parent = self
        r = [{'title': self.name, 'link': self.path}]
        # r = []
        while parent is not None:
            r.append({'title': parent.name, 'link': parent.path})
            parent = parent.parent

        return r[:0:-1]

    def create_slug(self):
        if self.slug == '':
            self.slug = slugify(unidecode(self.name))

    def save(self, *args, **kwargs):
        if not self.id:
            self.pub_date = timezone.now()
        self.mod_date = timezone.now()
        self.create_slug()

        if self.parent:
            self.path = '%s/%s' % (self.parent.path, self.slug)
            self.full_name = '%s/%s' % (self.parent.full_name, self.safe_translation_getter('name', language_code='ru'))
        else:
            self.path = '/category/%s' % (self.slug)
            self.full_name = '%s' % (self.safe_translation_getter('name', language_code='ru'))

        c = super(Category, self).save(*args, **kwargs)

        for child in self.get_children():
            child.save()

        return c

    def __str__(self):
        parent = self
        r = []
        while parent is not None:
            r.append(parent.safe_translation_getter('name', language_code='ru'))
            parent = parent.parent
        return '/'.join(r[::-1])

    def __unicode__(self):
        return self.__str__()

    def get_path(self):
        return '/category/' + self.path

    class Meta:
        verbose_name = 'категории'
        verbose_name_plural = 'категории'


class Color(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Цвет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'Цвета'


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название')
    enable = models.BooleanField(default=True, verbose_name='Показывать')
    slug = models.SlugField(max_length=128, blank=True, verbose_name='ЧПУ ссылка')

    def create_slug(self):
        if self.slug == '':
            self.slug = slugify(unidecode(self.name))

    def save(self, *args, **kwargs):
        self.create_slug()
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class SexChoise(models.TextChoices):
    MALE = 'Мужское'
    FEMALE = 'Женское'
    KIDS = 'Детское'
    UNISEX = 'Унисекс'


class Product(TranslatableModel):
    sku = models.CharField(max_length=256, unique=True, verbose_name='Артикул')
    model = models.CharField(blank=False, default='', max_length=128, verbose_name='Модель')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, verbose_name='Бренд')
    # price = models.IntegerField(blank=True, default=0, verbose_name='Цена')
    translations = TranslatedFields(
        description=models.TextField(blank=True, default='', verbose_name='Описание'),
        content=models.TextField(blank=True, default='', verbose_name='Состав'),
    )

    categories = models.ManyToManyField(
        Category,
        blank=False,
        related_name='products',
        verbose_name='Категории',
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='products',
        verbose_name='Теги'
    )

    colors = models.ManyToManyField(
        Color,
        blank=True,
        related_name='products',
        verbose_name='Цвета'
    )
    sex = models.CharField(
        max_length=10,
        choices=SexChoise.choices,
        default=SexChoise.MALE,
    )

    thumbnail = models.OneToOneField(
        MediaFile,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="product_thumnail",
        verbose_name='Превью'
    )
    media_files = models.ManyToManyField(
        MediaFile,
        blank=True,
        related_name="product_media_files",
        verbose_name='Медиафайлы'
    )

    total_count = models.IntegerField(verbose_name='Остаток', default=0)

    # myprice = models.OneToOneField(
    #     Price,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     related_name="product_price",
    #     verbose_name='Цены'
    # )

    price_ret = models.IntegerField(blank=False, default=0, verbose_name='Розничная цена')
    price_ret_sale = models.IntegerField(blank=False, default=0, verbose_name='Розничная цена, с учетом скидки')
    price_opt_m = models.IntegerField(blank=False, default=0, verbose_name='Мелкий Опт')
    price_opt_1 = models.IntegerField(blank=False, default=0, verbose_name='Опт от 11000')
    price_opt_2 = models.IntegerField(blank=False, default=0, verbose_name='- 3% от 30000')
    price_opt_3 = models.IntegerField(blank=False, default=0, verbose_name='- 7% от 70000')
    price_opt_4 = models.IntegerField(blank=False, default=0, verbose_name='- 11% от 110000')

    size_ns = models.IntegerField(blank=False, default=0, verbose_name='Без размера')
    size_4xs = models.IntegerField(blank=False, default=0, verbose_name='4XS размер')
    size_3xs = models.IntegerField(blank=False, default=0, verbose_name='3XS размер')
    size_2xs = models.IntegerField(blank=False, default=0, verbose_name='2XS размер')
    size_xs = models.IntegerField(blank=False, default=0, verbose_name='XS размер')
    size_s = models.IntegerField(blank=False, default=0, verbose_name='S размер')
    size_m = models.IntegerField(blank=False, default=0, verbose_name='M размер')
    size_l = models.IntegerField(blank=False, default=0, verbose_name='L размер')
    size_xl = models.IntegerField(blank=False, default=0, verbose_name='XL размер')
    size_2xl = models.IntegerField(blank=False, default=0, verbose_name='2XL размер')
    size_3xl = models.IntegerField(blank=False, default=0, verbose_name='3XL размер')
    size_4xl = models.IntegerField(blank=False, default=0, verbose_name='4XL размер')
    size_5xl = models.IntegerField(blank=False, default=0, verbose_name='5XL размер')
    size_6xl = models.IntegerField(blank=False, default=0, verbose_name='6XL размер')

    new = models.BooleanField(default=True, verbose_name='Новинка')
    hit = models.BooleanField(default=False, verbose_name='Хит')
    sale = models.BooleanField(default=False, verbose_name='Sale')
    glow_in_the_dark = models.BooleanField(default=True, verbose_name='Светится в темноте')
    glow_in_the_uv = models.BooleanField(default=True, verbose_name='Светится в ультрафиолете')

    enable = models.BooleanField(default=True, verbose_name='Показывать')
    slug = models.SlugField(max_length=128, blank=True, verbose_name='ЧПУ ссылка')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    mod_date = models.DateTimeField(auto_now=True, verbose_name='Изменен')

    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок сортировки')

    def create_slug(self):
        if self.slug == '':
            self.slug = slugify(unidecode(self.sku))

    def save(self, *args, **kwargs):
        if not self.id:
            self.pub_date = timezone.now()
        self.mod_date = timezone.now()
        self.create_slug()

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        # return self.safe_translation_getter('model', 'ru')
        # return self.model
        return self.sku

    class Meta:
        # ordering = ['my_order',]
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
