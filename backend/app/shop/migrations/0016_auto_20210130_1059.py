# Generated by Django 3.1.4 on 2021-01-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_delete_tagtranslation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='code',
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default='', max_length=128, unique=True, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
