# Generated by Django 3.1.4 on 2021-01-27 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20210127_1830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterModelOptions(
            name='producttranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'продукт Translation'},
        ),
    ]
