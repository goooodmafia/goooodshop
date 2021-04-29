# Generated by Django 3.1.6 on 2021-04-28 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20210422_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_ret', models.IntegerField(default=0, verbose_name='Розничная цена')),
                ('price_opt_m', models.IntegerField(default=0, verbose_name='Мелкий Опт')),
                ('price_opt_1', models.IntegerField(default=0, verbose_name='Опт от 11000')),
                ('price_opt_2', models.IntegerField(default=0, verbose_name='Опт от 30000')),
                ('price_opt_3', models.IntegerField(default=0, verbose_name='Опт от 70000')),
                ('price_opt_4', models.IntegerField(default=0, verbose_name='Опт от 110000')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='myprice',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_price', to='shop.price', verbose_name='Цены'),
        ),
    ]
