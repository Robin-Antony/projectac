# Generated by Django 3.2.15 on 2022-10-28 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20221027_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.order'),
        ),
    ]