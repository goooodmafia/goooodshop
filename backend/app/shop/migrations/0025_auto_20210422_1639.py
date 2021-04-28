# Generated by Django 3.1.6 on 2021-04-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20210403_0812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['my_order'], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]