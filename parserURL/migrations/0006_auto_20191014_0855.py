# Generated by Django 2.2.6 on 2019-10-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserURL', '0005_auto_20191014_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(verbose_name='Время начала'),
        ),
    ]