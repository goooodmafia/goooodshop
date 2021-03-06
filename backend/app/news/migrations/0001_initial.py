# Generated by Django 3.1.6 on 2021-04-22 21:58

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0026_auto_20210422_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='Ссылка')),
                ('slug', models.SlugField(blank=True, max_length=256, unique=True)),
                ('enable', models.BooleanField(default=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('image', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_image', to='shop.mediafile', verbose_name='КДПВ')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NewsTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='news.news')),
            ],
            options={
                'verbose_name': 'новость Translation',
                'db_table': 'news_news_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
