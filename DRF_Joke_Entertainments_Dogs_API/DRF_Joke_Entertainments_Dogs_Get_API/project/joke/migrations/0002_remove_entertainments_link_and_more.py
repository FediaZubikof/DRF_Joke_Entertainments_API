# Generated by Django 4.2.7 on 2023-11-13 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entertainments',
            name='link',
        ),
        migrations.AlterField(
            model_name='entertainments',
            name='start_data',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 19, 36, 42, 962907), null=True, verbose_name='Время и дата создания запроса.'),
        ),
        migrations.AlterField(
            model_name='joke',
            name='joke_start_data',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 19, 36, 42, 961905), null=True, verbose_name='Дата создания'),
        ),
    ]