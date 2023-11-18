from django.db import models

from main.models import City, Client, EstablishmentRates
from django.db.models import Q


def banquet_logo_upload_to(instance, filename):
    client_name = instance.client.name if instance.client else instance.name + '_has_not_menu'
    return f"{client_name.replace(' ', '_').capitalize()}/logo/banquet_{filename}"


def subhall_photo_upload_to(instance, filename):
    client_name = instance.banquet_card.client.name if instance.banquet_card and instance.banquet_card.client else 'unknown'
    return f"{client_name.replace(' ', '_').capitalize()}/banquet_photo/{filename}"


class BanquetCard(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название банкетного зала')
    client = models.ForeignKey(to=Client, verbose_name='Зал заведения:', on_delete=models.CASCADE, blank=True,
                               null=True)
    logo = models.ImageField(verbose_name='Лого', upload_to=banquet_logo_upload_to, blank=True, null=True)
    capacity = models.PositiveIntegerField(verbose_name='Вместимость')
    price_min = models.PositiveIntegerField(verbose_name='Мин. цена за человека')
    price_max = models.PositiveIntegerField(verbose_name='Макс. цена за человека')
    city = models.ForeignKey(City, models.CASCADE, verbose_name="Город", blank=True, null=True)
    status = models.BooleanField(verbose_name='Активен')
    url_name = models.CharField(max_length=30, verbose_name="/url", unique=True)

    working_time = models.CharField(max_length=20, verbose_name="Рабочее время", blank=True, null=True)
    address = models.CharField(max_length=50, verbose_name="Адрес", blank=True, null=True, unique=True)

    whatsapp = models.CharField(max_length=50, verbose_name="WhatsApp", blank=True, null=True, unique=True)
    inst = models.CharField(max_length=100, verbose_name="Instagram", blank=True, null=True, unique=True)
    two_gis = models.CharField(max_length=150, verbose_name="2gis", blank=True, null=True, unique=True)
    phone = models.CharField(max_length=30, verbose_name="Телефон", blank=True, null=True, unique=True)

    z_index = models.IntegerField(verbose_name="Порядковый №", blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Карточку банкетного зала'
        verbose_name_plural = 'Карточки банкетных залов'

    def __str__(self):
        return self.name


class KitchenType(models.Model):
    kitchen_type = models.CharField(max_length=256, verbose_name='Вид кухни')

    class Meta:
        verbose_name = 'Вид кухни'
        verbose_name_plural = 'Виды кухни'

    def __str__(self):
        return self.kitchen_type


class FeaturesOfTheBanquetHall(models.Model):
    features_name = models.CharField(max_length=256, verbose_name='Особенности банкетного зала')

    class Meta:
        verbose_name = 'Особенность банкетного зала'
        verbose_name_plural = 'Особенности банкетных залов'

    def __str__(self):
        return self.features_name


GUARDED = 'Охраняемая'
UNGUARDED = 'Неохраняемая'

PAID = 'Платная'
FREE = 'Бесплатная'

PARKING_1_CHOICES = [
    (GUARDED, 'Охраняемая'),
    (UNGUARDED, 'Неохраняемая'),
]

PARKING_2_CHOICES = [
    (PAID, 'Платная'),
    (FREE, 'Бесплатная'),
]


class Banquet(models.Model):
    banquet_card = models.ForeignKey(to=BanquetCard, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name='Карточка банкетного зала')
    name = models.CharField(max_length=256, verbose_name='Название зала')
    parking_1 = models.CharField(blank=True, null=True, choices=PARKING_1_CHOICES, max_length=256,
                                 verbose_name='Парковка: Охраняемая/Неохраняемая')
    parking_2 = models.CharField(blank=True, null=True, choices=PARKING_2_CHOICES, max_length=256,
                                 verbose_name='Парковка: Платная/Бесплатная')
    kitchen_types = models.ManyToManyField(to=KitchenType, verbose_name='Виды кухни', blank=True, null=True,)
    features_name = models.ManyToManyField(to=FeaturesOfTheBanquetHall, verbose_name='Особенности банкетного зала', blank=True, null=True)
    memorials = models.CharField(max_length=256, blank=True, null=True, verbose_name='Стоимость поминок(xxxx-xxxx)')
    sub_hall_capacity = models.CharField(max_length=256, blank=True, null=True, verbose_name='Вместимость зала')
    sub_hall_price_for_person = models.CharField(max_length=256, blank=True, null=True,
                                                 verbose_name='Цена за человека(xxxx-xxxx)')

    description = models.CharField(max_length=256, blank=True, null=True, verbose_name='Описание пзала', )
    hall_no = models.IntegerField(blank=True, null=True, verbose_name="№ Зала")

    photo1 = models.ImageField(verbose_name='Фото 1', upload_to=subhall_photo_upload_to, blank=True, null=True)
    photo2 = models.ImageField(verbose_name='Фото 2', upload_to=subhall_photo_upload_to, blank=True, null=True)
    photo3 = models.ImageField(verbose_name='Фото 3', upload_to=subhall_photo_upload_to, blank=True, null=True)
    photo4 = models.ImageField(verbose_name='Фото 4', upload_to=subhall_photo_upload_to, blank=True, null=True)
    photo5 = models.ImageField(verbose_name='Фото 5', upload_to=subhall_photo_upload_to, blank=True, null=True)
    photo6 = models.ImageField(verbose_name='Фото 6', upload_to=subhall_photo_upload_to, blank=True, null=True)

    class Meta:
        verbose_name = 'Банкетный зал'
        verbose_name_plural = 'Банкетные залы'

    def __str__(self):
        return self.name


