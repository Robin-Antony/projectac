# Generated by Django 3.2.14 on 2022-10-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rating_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='body',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
