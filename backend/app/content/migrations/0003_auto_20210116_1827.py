# Generated by Django 3.1.4 on 2021-01-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20210106_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='position',
            field=models.CharField(choices=[('HEADER_TOP', 'Над заголовком'), ('HEADER_BOTTOM', 'Под заголовком'), ('DEFAULT_TOP', 'Выше контента'), ('DEFAULT_BOTTOM', 'Ниже контета'), ('FOOTER_TOP', 'Над подвалом'), ('FOOTER_BOTTOM', 'Под подвалом')], default='DEFAULT_TOP', max_length=32, verbose_name='позиция'),
        ),
    ]
