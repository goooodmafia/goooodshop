# Generated by Django 3.1.6 on 2021-05-24 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210524_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='birthdate',
            new_name='birth_date',
        ),
    ]