# Generated by Django 3.1.4 on 2021-01-30 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20210130_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
    ]
