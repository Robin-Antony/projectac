# Generated by Django 3.2.14 on 2022-10-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20221026_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField(blank=True, max_length=500, null=True, verbose_name='address')),
                ('problem', models.TextField(blank=True, max_length=700, null=True, verbose_name='How Can We Help You?')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rated', models.IntegerField()),
            ],
        ),
    ]
