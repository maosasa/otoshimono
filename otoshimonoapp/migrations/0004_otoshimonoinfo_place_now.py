# Generated by Django 3.2.10 on 2021-12-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otoshimonoapp', '0003_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='otoshimonoinfo',
            name='place_now',
            field=models.CharField(default='見つけた場所と同じ', max_length=200),
        ),
    ]