from django.db import models

from main.models.utils.images_upload import client_logo_upload_to


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")
    city = models.ForeignKey("main.City", models.CASCADE, verbose_name="Город")
    logo = models.ImageField(upload_to=client_logo_upload_to, verbose_name="Лого")
    description = models.TextField(verbose_name="Описание", max_length=100)
    working_time = models.CharField(max_length=20, verbose_name="Рабочее время")
    address = models.CharField(max_length=50, verbose_name="Адрес")
    phone = models.DecimalField(max_digits=15, decimal_places=0, verbose_name="Телефон")
    inst = models.CharField(max_length=100, blank=True, verbose_name="Instagram")
    two_gis = models.CharField(
        max_length=150, verbose_name="2gis", unique=True, blank=True, null=True
    )
    status = models.BooleanField(verbose_name="Активен")
    outside = models.BooleanField(verbose_name="Самовывоз")
    delivery = models.BooleanField(verbose_name="Доставка")
    url_name = models.CharField(max_length=30, verbose_name="/url", unique=True)
    tarif_number = models.ForeignKey(
        "main.EstablishmentRates",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Тариф",
    )
    z_index = models.IntegerField(verbose_name="Порядковый №", default=1)

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"

    def __str__(self):
        return self.name
