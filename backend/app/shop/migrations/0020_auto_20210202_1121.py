# Generated by Django 3.1.4 on 2021-02-02 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20210202_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='thumnail',
            new_name='thumbnail',
        ),
    ]
