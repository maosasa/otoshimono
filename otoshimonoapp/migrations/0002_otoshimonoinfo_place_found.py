# Generated by Django 3.2.10 on 2021-12-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otoshimonoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='otoshimonoinfo',
            name='place_found',
            field=models.CharField(default='', max_length=200),
        ),
    ]
