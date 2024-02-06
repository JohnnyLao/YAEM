from django.db import models

from banquets.models.utils.choices import (HallNumber, ParkingType1,
                                           ParkingType2)
from banquets.models.utils.images_upload import subhall_photo_upload_to


class Banquet(models.Model):
    banquet_card = models.ForeignKey(
        to="banquets.BanquetCard",
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
    kitchen_types = models.ManyToManyField(
        to="banquets.KitchenType", verbose_name="Виды кухни"
    )
    features_name = models.ManyToManyField(
        to="banquets.FeaturesOfTheBanquetHall",
        verbose_name="Особенности банкетного зала",
    )
    parking_1 = models.CharField(
        blank=True,
        null=True,
        choices=ParkingType1.choices,
        max_length=256,
        verbose_name="Парковка: Охраняемая/Неохраняемая",
        default=ParkingType1.UNGUARDED_RU,
    )
    parking_2 = models.CharField(
        blank=True,
        null=True,
        choices=ParkingType2.choices,
        max_length=256,
        verbose_name="Парковка: Платная/Бесплатная",
        default=ParkingType2.FREE_RU,
    )

    memorials = models.CharField(
        max_length=256,
        verbose_name="Стоимость поминок(XXXX - XXXX)",
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
        choices=HallNumber.choices, default=HallNumber.HALL_1, verbose_name="№ Зала"
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
        ordering = ("id",)

    def __str__(self):
        return self.name
