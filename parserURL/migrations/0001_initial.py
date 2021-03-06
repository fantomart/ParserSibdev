# Generated by Django 2.2.6 on 2019-10-14 05:44

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=100, verbose_name='URL')),
                ('minutes', models.PositiveIntegerField(blank=True, default=0, verbose_name='Минуты')),
                ('seconds', models.PositiveIntegerField(blank=True, default=0, verbose_name='Секунды')),
                ('start_time', models.DateTimeField(default=datetime.datetime(2019, 10, 14, 8, 44, 38, 810220), verbose_name='Время начала')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('code', models.CharField(max_length=100, verbose_name='Кодировка')),
                ('header', models.CharField(blank=True, max_length=100, verbose_name='H1')),
                ('report', models.CharField(default='', max_length=100, verbose_name='Отчет о выполнении')),
                ('is_done', models.BooleanField(default=False, verbose_name='Выполнено')),
            ],
        ),
    ]
