# Generated by Django 4.2 on 2023-05-01 18:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers_network', '0002_alter_product_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkobject',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='suppliers_network.networkobject', validators=[django.core.validators.MaxValueValidator(limit_value=models.PositiveSmallIntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], default=0, verbose_name='Уровень'), message='Неверная иерархия поставщиков.')], verbose_name='Поставщик'),
        ),
    ]