# Generated by Django 3.2.5 on 2021-08-04 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210804_1033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name': '販売商品', 'verbose_name_plural': '販売商品'},
        ),
    ]