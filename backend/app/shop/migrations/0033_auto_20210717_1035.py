# Generated by Django 3.1.6 on 2021-07-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_product_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_ret_sale',
            field=models.IntegerField(default=0, verbose_name='Розничная цена, с учетом скидки'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_5xl',
            field=models.IntegerField(default=0, verbose_name='5XL размер'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_6xl',
            field=models.IntegerField(default=0, verbose_name='6XL размер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_opt_2',
            field=models.IntegerField(default=0, verbose_name='- 3% от 30000'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_opt_3',
            field=models.IntegerField(default=0, verbose_name='- 7% от 70000'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_opt_4',
            field=models.IntegerField(default=0, verbose_name='- 11% от 110000'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sex',
            field=models.CharField(choices=[('Мужское', 'Male'), ('Женское', 'Female'), ('Детское', 'Kids'), ('Унисекс', 'Unisex')], default='Мужское', max_length=10),
        ),
    ]