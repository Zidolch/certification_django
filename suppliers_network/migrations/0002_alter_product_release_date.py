# Generated by Django 4.2 on 2023-05-01 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers_network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата выхода'),
        ),
    ]
