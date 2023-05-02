from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)
    model = models.CharField(verbose_name="Модель", max_length=200)
    release_date = models.DateTimeField(verbose_name="Дата выхода", default=timezone.now)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class NetworkObject(models.Model):
    class Level(models.IntegerChoices):
        factory = 0, "Завод"
        network_shop = 1, "Розничная сеть"
        sole_proprietor = 2, "Индивидуальный предприниматель"

    name = models.CharField(verbose_name="Название", max_length=200)
    email = models.EmailField(verbose_name="Email", max_length=200)
    country = models.CharField(verbose_name="Страна", max_length=200)
    city = models.CharField(verbose_name="Город", max_length=200)
    street = models.CharField(verbose_name="Улица", max_length=200)
    house = models.CharField(verbose_name="Дом", max_length=200)

    products = models.ManyToManyField(Product, verbose_name="Товары")
    level = models.IntegerField(verbose_name="Уровень", choices=Level.choices, default=Level.factory)

    supplier = models.ForeignKey(
        'NetworkObject', verbose_name="Поставщик", on_delete=models.PROTECT, null=True, blank=True,
    )
    debt = models.DecimalField(
        verbose_name="Задолженность", decimal_places=2, max_digits=20, null=True, blank=True
    )

    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def clean(self):
        if self.supplier:
            supplier_level = NetworkObject.objects.values('level').get(id=self.supplier_id)['level']
            if self.level - supplier_level not in [0, 1]:
                raise ValidationError(f'Поставщик находится на недопустимом уровне иерархии.')
        elif self.debt:
            raise ValidationError('Невозможна задолженность без поставщика.')

    class Meta:
        verbose_name = 'Элемент сети'
        verbose_name_plural = 'Элементы сети'

    def __str__(self):
        return self.name
