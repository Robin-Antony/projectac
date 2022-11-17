# Generated by Django 3.2.15 on 2022-11-01 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20221031_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accurorder',
            name='user',
        ),
        migrations.AddField(
            model_name='accurorder',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.staff'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
