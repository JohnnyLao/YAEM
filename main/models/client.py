from crum import get_current_user
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from main.models.utils.images_upload import client_logo_upload_to


class Client(models.Model):
    # main info
    # relation with user
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        verbose_name='Владелец',
        help_text='Автоматическое заполнение',
        # all user establishments
        related_name='get_user_establishments',
    )
    # establishment name
    name = models.CharField(max_length=20, verbose_name="Наименование")
    # establishment URL name
    url_name = models.CharField(
        max_length=30,
        verbose_name="/url",
        unique=True,
        help_text="Путь: yaem.kz/***/menu",
    )
    # establishment city
    city = models.ForeignKey(
        "main.City", models.SET_NULL, verbose_name="Город", null=True
    )

    # remove before ..
    working_time = models.CharField(
        max_length=20,
        verbose_name="Рабочее время",
        help_text="Формат: '00:00-24:00'",
        blank=True,
    )
    # working time
    work_time_start = models.TimeField(
        verbose_name="Начало работы заведения",
        help_text="Формат: '00:00-24:00'",
        blank=True,
        default=timezone.now,
    )
    work_time_end = models.TimeField(
        verbose_name="Конец работы заведения",
        help_text="Формат: '00:00-24:00'",
        blank=True,
        default=timezone.now,
    )

    # secondary info
    # establishment logo
    logo = models.ImageField(
        upload_to=client_logo_upload_to,
        verbose_name="Лого",
        help_text="Для отображения на главной странице",
        blank=True,
    )
    # establishment description
    description = models.TextField(verbose_name="Описание", max_length=200, blank=True)
    address = models.CharField(
        max_length=50, verbose_name="Адрес", help_text="Улица, дом", blank=True
    )
    # establishment phone
    phone = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        verbose_name="Телефон",
        help_text="Формат: '77015302812' (без +)",
        blank=True,
        null=True,
    )
    # establishment inst
    inst = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Instagram",
        help_text="Ссылка на Instagram",
    )
    # establishment two gis
    two_gis = models.CharField(
        max_length=150,
        verbose_name="2gis",
        blank=True,
        null=True,
        help_text="Ссылка на 2Gis",
    )
    # establishment outside
    outside = models.BooleanField(
        verbose_name="Самовывоз", help_text="Значок Самовывоза", default=False
    )
    # establishment delivery
    delivery = models.BooleanField(
        verbose_name="Доставка", help_text="Значок Доставки", default=False
    )
    # establishment service
    service = models.PositiveSmallIntegerField(
        default=0, verbose_name='% за обслуживание', blank=True
    )
    # establishment wifi
    wifi = models.CharField(verbose_name='WiFi', blank=True, max_length=30)
    wifi_password = models.CharField(
        verbose_name='WiFi - пароль', blank=True, max_length=30
    )

    # admin info
    # establishment tarif
    tarif_number = models.ForeignKey(
        "main.EstablishmentRates",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Тариф",
    )
    # establishment is active
    status = models.BooleanField(
        verbose_name="Активен",
        help_text="Отображение при поиске в Delivery",
        default=False,
    )
    # establishment paid at
    paid_at = models.DateField(blank=True, verbose_name='Время оплаты', null=True)
    # establishment translated
    translated = models.BooleanField(
        verbose_name="Перевод", default=False, help_text="Значок перевода на 3 языка"
    )
    # sorted
    z_index = models.IntegerField(
        verbose_name="Порядковый №",
        default=100,
        help_text="Алматы 1-10, Астана 11-20, Караганда 21-30",
        blank=True,
    )
    # time
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name='Время создания', null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, verbose_name='Время обновления', null=True
    )

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"
        ordering = ('z_index',)

    # on save client objects, create relation between current user-client
    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user = get_current_user()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
