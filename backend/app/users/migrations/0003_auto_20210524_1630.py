# Generated by Django 3.1.6 on 2021-05-24 16:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(default='', verbose_name='Адресс'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата рожения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='', max_length=150, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='second_name',
            field=models.CharField(default='', max_length=150, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
    ]