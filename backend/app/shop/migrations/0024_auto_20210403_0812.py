# Generated by Django 3.1.6 on 2021-04-03 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20210320_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media_files',
            field=models.ManyToManyField(blank=True, related_name='product_media_files', to='shop.MediaFile', verbose_name='Медиафайлы'),
        ),
    ]
