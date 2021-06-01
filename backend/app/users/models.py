from datetime import date

from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField('Имя', max_length=150)

    first_name = models.CharField('Имя', max_length=150, default='', blank=True)
    second_name = models.CharField('Имя', max_length=150, default='', blank=True)
    phone = models.CharField('Телефон', max_length=20)

    address = models.TextField('Адресс', default='', blank=True)
    birth_date = models.DateField('Дата рожения', default=date(1800, 1, 1), blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
