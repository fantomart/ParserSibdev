# Generated by Django 2.2.6 on 2019-10-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserURL', '0006_auto_20191014_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(verbose_name='Выполнено'),
        ),
        migrations.AlterField(
            model_name='task',
            name='minutes',
            field=models.PositiveIntegerField(blank=True, verbose_name='Минуты'),
        ),
        migrations.AlterField(
            model_name='task',
            name='report',
            field=models.CharField(max_length=100, verbose_name='Отчет о выполнении'),
        ),
        migrations.AlterField(
            model_name='task',
            name='seconds',
            field=models.PositiveIntegerField(blank=True, verbose_name='Секунды'),
        ),
    ]