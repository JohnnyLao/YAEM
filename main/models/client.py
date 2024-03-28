from django.contrib.auth import get_user_model
from django.db import models
from main.models.utils.images_upload import client_logo_upload_to
from django.utils import timezone

class Client(models.Model):
    # main info
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        verbose_name='Аккаунт',
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=20, verbose_name="Наименование")
    url_name = models.CharField(
        max_length=30,
        verbose_name="/url",
        unique=True,
        help_text="Путь: yaem.kz/***/menu",
    )

    city = models.ForeignKey("main.City", models.SET_NULL, verbose_name="Город", null=True)


    # remove before ..
    working_time = models.CharField(
        max_length=20, verbose_name="Рабочее время", help_text="Формат: '00:00-24:00'", blank=True
    )

    work_time_start = models.TimeField(
        verbose_name="Начало работы заведения", help_text="Формат: '00:00-24:00'", blank=True, default=timezone.now
    )
    work_time_end = models.TimeField(
        verbose_name="Конец работы заведения", help_text="Формат: '00:00-24:00'", blank=True, default=timezone.now
    )

    # secondary info
    logo = models.ImageField(
        upload_to=client_logo_upload_to,
        verbose_name="Лого",
        help_text="Для отображения на главной странице",
        blank=True,
    )
    description = models.TextField(verbose_name="Описание", max_length=200, blank=True)
    address = models.CharField(
        max_length=50, verbose_name="Адрес", help_text="Улица, дом", blank=True
    )
    phone = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        verbose_name="Телефон",
        help_text="Формат: '77015302812' (без +)", blank=True, null=True
    )
    inst = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Instagram",
        help_text="Ссылка на Instagram",
    )
    two_gis = models.CharField(
        max_length=150,
        verbose_name="2gis",
        blank=True,
        null=True,
        help_text="Ссылка на 2Gis",
    )

    outside = models.BooleanField(
        verbose_name="Самовывоз", help_text="Значок Самовывоза", default=False
    )

    delivery = models.BooleanField(verbose_name="Доставка", help_text="Значок Доставки", default=False)

    tarif_number = models.ForeignKey(
        "main.EstablishmentRates",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Тариф",
    )

    service = models.PositiveSmallIntegerField(
        default=0, verbose_name='% за обслуживание', blank=True
    )

    wifi = models.CharField(verbose_name='WiFi', blank=True, max_length=30)
    wifi_password = models.CharField(
        verbose_name='WiFi - пароль', blank=True, max_length=30
    )

    # admin info
    status = models.BooleanField(
        verbose_name="Активен", help_text="Отображение при поиске в Delivery", default=False
    )
    paid_at = models.DateField(blank=True, verbose_name='Время оплаты', null=True)
    translated = models.BooleanField(
        verbose_name="Перевод", default=False, help_text="Значок перевода на 3 языка"
    )
    z_index = models.IntegerField(
        verbose_name="Порядковый №",
        default=100,
        help_text="Алматы 1-10, Астана 11-20, Караганда 21-30", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Время создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Время обновления', null=True)

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"
        ordering = ('z_index',)

    def __str__(self):
        return self.name
