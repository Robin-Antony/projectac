# Generated by Django 3.2.15 on 2022-11-01 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20221101_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_price',
            field=models.FloatField(default=0),
        ),
    ]
