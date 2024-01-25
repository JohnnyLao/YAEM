from django.db import models
from django.utils.translation import gettext_lazy as _

from main.models import City, Client, EstablishmentRates


def banquet_logo_upload_to(instance, filename):
    client_name = (
        instance.client.name if instance.client else instance.name + "_has_not_menu"
    )
    return f"{client_name.replace(' ', '_').capitalize()}/logo/banquet_{filename}"


def subhall_photo_upload_to(instance, filename):
    client_name = (
        instance.banquet_card.client.name
        if instance.banquet_card and instance.banquet_card.client
        else "unknown"
    )
    return f"{client_name.replace(' ', '_').capitalize()}/banquet_photo/{filename}"


class BanquetCard(models.Model):
    client = models.ForeignKey(
        to=Client,
        verbose_name="Зал заведения:",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(City, models.CASCADE, verbose_name="Город")
    name = models.CharField(
        max_length=100, unique=True, verbose_name="Название банкетного зала"
    )
    url_name = models.CharField(
        max_length=30, verbose_name="/url=client url", unique=True
    )
    logo = models.ImageField(verbose_name="Лого", upload_to=banquet_logo_upload_to)
    photo1 = models.ImageField(
        verbose_name="Фото 1", upload_to=banquet_logo_upload_to, blank=True, null=True
    )
    photo2 = models.ImageField(
        verbose_name="Фото 2", upload_to=banquet_logo_upload_to, blank=True, null=True
    )
    photo3 = models.ImageField(
        verbose_name="Фото 3", upload_to=banquet_logo_upload_to, blank=True, null=True
    )
    capacity = models.PositiveIntegerField(verbose_name="Вместимость")
    min_capacity = models.PositiveIntegerField(
        verbose_name="Минимальная вместимость", blank=True, null=True
    )
    price_max = models.PositiveIntegerField(verbose_name="Макс. цена за человека")
    price_min = models.PositiveIntegerField(verbose_name="Мин. цена за человека")
    status = models.BooleanField(verbose_name="Активен")
    working_time = models.CharField(
        max_length=20, verbose_name="Рабочее время", blank=True, null=True
    )
    address = models.CharField(
        max_length=50, verbose_name="Адрес", blank=True, null=True, unique=True
    )
    whatsapp = models.CharField(
        max_length=50, verbose_name="WhatsApp", blank=True, null=True, unique=True
    )
    inst = models.CharField(
        max_length=100, verbose_name="Instagram", blank=True, null=True, unique=True
    )
    two_gis = models.CharField(
        max_length=150, verbose_name="2gis", blank=True, null=True, unique=True
    )
    phone = models.CharField(
        max_length=30, verbose_name="Телефон", blank=True, null=True, unique=True
    )
    z_index = models.IntegerField(
        verbose_name="Порядковый №", blank=True, null=True, default=11
    )

    class Meta:
        verbose_name = "Карточку банкетного зала"
        verbose_name_plural = "Карточки банкетных залов"

    def __str__(self):
        return self.name


class KitchenType(models.Model):
    kitchen_type = models.CharField(max_length=256, verbose_name="Вид кухни")

    class Meta:
        verbose_name = "Вид кухни"
        verbose_name_plural = "Виды кухни"

    def __str__(self):
        return self.kitchen_type


class FeaturesOfTheBanquetHall(models.Model):
    features_name = models.CharField(
        max_length=256, verbose_name="Особенности банкетного зала"
    )

    class Meta:
        verbose_name = "Особенность банкетного зала"
        verbose_name_plural = "Особенности банкетных залов"

    def __str__(self):
        return self.features_name


GUARDED_RU, GUARDED_EN, GUARDED_KK = "Охраняемая", "Guarded", "Қорғалған"
UNGUARDED_RU, UNGUARDED_EN, UNGUARDED_KK = "Неохраняемая", "Unguarded", "Күзетсіз"

PAID_RU, PAID_EN, PAID_KK = "Платная", "Paid", "Ақылы"
FREE_RU, FREE_EN, FREE_KK = "Бесплатная", "Free", "Тегін"

PARKING_1_CHOICES = [
    (GUARDED_RU, "Охраняемая"),
    (GUARDED_EN, "Guarded"),
    (GUARDED_KK, "Қорғалған"),
    (UNGUARDED_RU, "Неохраняемая"),
    (UNGUARDED_EN, "Unguarded"),
    (UNGUARDED_KK, "Күзетсіз"),
]

PARKING_2_CHOICES = [
    (PAID_RU, "Платная"),
    (PAID_EN, "Paid"),
    (PAID_KK, "Ақылы"),
    (FREE_RU, "Бесплатная"),
    (FREE_EN, "Free"),
    (FREE_KK, "Тегін"),
]

HALL_NUMBER = [
    (1, "Зал 1"),
    (2, "Зал 2"),
    (3, "Зал 3"),
    (4, "Зал 4"),
]


class Banquet(models.Model):
    banquet_card = models.ForeignKey(
        to=BanquetCard,
        on_delete=models.CASCADE,
        verbose_name="Карточка банкетного зала",
        null=True,
    )
    name = models.CharField(
        max_length=256, verbose_name="Название зала", default="Банкетный зал"
    )
    description = models.TextField(
        default="Добро пожаловать! Всегда рады видеть вас.",
        verbose_name="Описание зала",
        blank=True,
        null=True,
    )
    kitchen_types = models.ManyToManyField(to=KitchenType, verbose_name="Виды кухни")
    features_name = models.ManyToManyField(
        to=FeaturesOfTheBanquetHall, verbose_name="Особенности банкетного зала"
    )
    parking_1 = models.CharField(
        blank=True,
        null=True,
        choices=PARKING_1_CHOICES,
        max_length=256,
        verbose_name="Парковка: Охраняемая/Неохраняемая",
        default="Неохраняемая",
    )
    parking_2 = models.CharField(
        blank=True,
        null=True,
        choices=PARKING_2_CHOICES,
        max_length=256,
        verbose_name="Парковка: Платная/Бесплатная",
        default="Бесплатная",
    )

    memorials = models.CharField(
        max_length=256,
        verbose_name="Стоимость поминок(XXXX-XXXX)",
        blank=True,
        null=True,
    )
    sub_hall_capacity = models.CharField(
        max_length=256, verbose_name="Вместимость зала(XXX)"
    )
    sub_hall_price_for_person = models.CharField(
        max_length=256, verbose_name="Цена за человека(XXXX-XXXX)"
    )
    hall_no = models.IntegerField(
        choices=HALL_NUMBER, default=HALL_NUMBER[0][0], verbose_name="№ Зала"
    )

    photo1 = models.ImageField(
        verbose_name="Фото 1", upload_to=subhall_photo_upload_to, blank=True, null=True
    )
    photo2 = models.ImageField(
        verbose_name="Фото 2", upload_to=subhall_photo_upload_to, blank=True, null=True
    )
    photo3 = models.ImageField(
        verbose_name="Фото 3", upload_to=subhall_photo_upload_to, blank=True, null=True
    )
    photo4 = models.ImageField(
        verbose_name="Фото 4", upload_to=subhall_photo_upload_to, blank=True, null=True
    )
    photo5 = models.ImageField(
        verbose_name="Фото 5", upload_to=subhall_photo_upload_to, blank=True, null=True
    )
    photo6 = models.ImageField(
        verbose_name="Фото 6", upload_to=subhall_photo_upload_to, blank=True, null=True
    )
    photo7 = models.ImageField(
        verbose_name="Фото 7", upload_to=subhall_photo_upload_to, blank=True, null=True
    )
    photo8 = models.ImageField(
        verbose_name="Фото 8", upload_to=subhall_photo_upload_to, blank=True, null=True
    )
    photo9 = models.ImageField(
        verbose_name="Фото 9", upload_to=subhall_photo_upload_to, blank=True, null=True
    )
    photo10 = models.ImageField(
        verbose_name="Фото 10", upload_to=subhall_photo_upload_to, blank=True, null=True
    )

    class Meta:
        verbose_name = "Банкетный зал"
        verbose_name_plural = "Банкетные залы"

    def __str__(self):
        return self.name
