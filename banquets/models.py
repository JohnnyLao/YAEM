from django.db import models

from main.models import City

CAPASITY_CHOICES = [
    (500, '500'),
    (1000, '1000'),
    (2000, '2000'),
]
PRICE_CHOICES = [
    (5000, '5000'),
    (8000, '8000'),
    (10000, '10000'),
]


def banquet_logo_upload_to(instance, filename):
    return f"{instance.name.replace(' ', '_').capitalize()}/logo/{filename}"


class Banquet(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название банкетного зала')
    description = models.CharField(max_length=256, blank=True, null=True, verbose_name='Описание')
    logo = models.ImageField(verbose_name='Лого', upload_to=banquet_logo_upload_to, blank=True, null=True)
    capacity = models.PositiveIntegerField(verbose_name='Вместимость', choices=CAPASITY_CHOICES)
    price = models.PositiveIntegerField(verbose_name='Цена за человека', choices=PRICE_CHOICES)
    city = models.ForeignKey(City, models.CASCADE, verbose_name="Город", blank=True, null=True)
    working_time = models.CharField(max_length=20, verbose_name="Рабочее время", blank=True, null=True)
    address = models.CharField(max_length=50, verbose_name="Адрес", blank=True, null=True, unique=True)
    phone = models.CharField(max_length=30, verbose_name="Телефон", blank=True, null=True, unique=True)
    inst = models.CharField(max_length=100, blank=True, null=True, verbose_name="Instagram")
    two_gis = models.CharField(max_length=150, verbose_name="2gis", unique=True, blank=True, null=True)
    status = models.BooleanField(verbose_name='Активен')
    url_name = models.CharField(max_length=30, verbose_name="/url", unique=True)
    z_index = models.IntegerField(verbose_name="Порядковый №")

    class Meta:
        verbose_name = 'Банкетный зал'
        verbose_name_plural = 'Банкетные залы'

    def __str__(self):
        return self.name
