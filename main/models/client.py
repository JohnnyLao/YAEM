from django.db import models

from main.models.utils.images_upload import client_logo_upload_to


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование")
    city = models.ForeignKey("main.City", models.CASCADE, verbose_name="Город")
    logo = models.ImageField(
        upload_to=client_logo_upload_to,
        verbose_name="Лого",
        help_text="Для отображения на главной странице",
    )
    description = models.TextField(verbose_name="Описание", max_length=200)
    working_time = models.CharField(
        max_length=20, verbose_name="Рабочее время", help_text="Формат: '00:00-24:00'"
    )
    address = models.CharField(
        max_length=50, verbose_name="Адрес", help_text="Улица, дом"
    )
    phone = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        verbose_name="Телефон",
        help_text="Формат: '77015302812' (без +)",
    )
    inst = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Instagram",
        help_text="Ссылка на Instagram",
    )
    two_gis = models.CharField(
        max_length=150,
        verbose_name="2gis",
        unique=True,
        blank=True,
        null=True,
        help_text="Ссылка на 2Gis",
    )
    status = models.BooleanField(
        verbose_name="Активен", help_text="Отображение при поиске в Delivery"
    )
    outside = models.BooleanField(
        verbose_name="Самовывоз", help_text="Значок Самовывоза"
    )
    delivery = models.BooleanField(verbose_name="Доставка", help_text="Значок Доставки")
    translated = models.BooleanField(
        verbose_name="Перевод", default=False, help_text="Значок перевода на 3 языка"
    )
    url_name = models.CharField(
        max_length=30,
        verbose_name="/url",
        unique=True,
        help_text="Путь: yaem.kz/***/menu",
    )
    tarif_number = models.ForeignKey(
        "main.EstablishmentRates",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Тариф",
    )
    service = models.PositiveSmallIntegerField(default=0, verbose_name='% за обслуживание', blank=True)
    z_index = models.IntegerField(
        verbose_name="Порядковый №",
        default=100,
        help_text="Алматы 1-10, Астана 11-20, Караганда 21-30",
    )

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"

    def __str__(self):
        return self.name
