from django.db import models

from main.models import City, Client

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
    return f"{instance.client.name.replace(' ', '_').capitalize()}/logo/banquet_{filename}"


def subhall_photo_upload_to(instance, filename):
    return f"{instance.banquet.client.name.replace(' ', '_').capitalize()}/subhall_photo/{filename}"


class Banquet(models.Model):
    # Общие данные для всех залов
    name = models.CharField(max_length=100, unique=True, verbose_name='Название банкетного зала')
    logo = models.ImageField(verbose_name='Лого', upload_to=banquet_logo_upload_to, blank=True, null=True)
    capacity = models.PositiveIntegerField(verbose_name='Вместимость')
    price_min = models.PositiveIntegerField(verbose_name='Мин. цена за человека')
    price_max = models.PositiveIntegerField(verbose_name='Макс. цена за человека')
    city = models.ForeignKey(City, models.CASCADE, verbose_name="Город", blank=True, null=True)
    working_time = models.CharField(max_length=20, verbose_name="Рабочее время", blank=True, null=True)
    address = models.CharField(max_length=50, verbose_name="Адрес", blank=True, null=True, unique=True)
    phone = models.CharField(max_length=30, verbose_name="Телефон", blank=True, null=True, unique=True)
    inst = models.CharField(max_length=100, blank=True, null=True, verbose_name="Instagram")
    two_gis = models.CharField(max_length=150, verbose_name="2gis", unique=True, blank=True, null=True)
    status = models.BooleanField(verbose_name='Активен')
    url_name = models.CharField(max_length=30, verbose_name="/url", unique=True)
    z_index = models.IntegerField(verbose_name="Порядковый №")

    client = models.ForeignKey(to=Client, verbose_name='Чей зал?', blank=True, null=True,
                               on_delete=models.CASCADE)

    subhalls = models.ManyToManyField('SubHall', related_name='banquets', verbose_name='Подзалы', blank=True, null=True)

    class Meta:
        verbose_name = 'Банкетный зал'
        verbose_name_plural = 'Банкетные залы'

    def __str__(self):
        return self.name


class SubHall(models.Model):
    # Уникальные данные для каждого подзала
    banquet = models.ForeignKey(to=Banquet, on_delete=models.CASCADE, verbose_name='Название банкетного зала')
    name = models.CharField(max_length=256, verbose_name='Название подзала')
    kitchen_type = models.CharField(max_length=256, blank=True, null=True, verbose_name='Виды кухни')
    memorials = models.CharField(max_length=256, blank=True, null=True, verbose_name='Стоимость поминок(xxxx-xxxx)')
    sub_hall_capacity = models.CharField(max_length=256, blank=True, null=True, verbose_name='Вместимость подзала')
    sub_hall_price_for_person = models.CharField(max_length=256, blank=True, null=True,
                                                 verbose_name='Цена за человека(xxxx-xxxx)')
    sub_hall_peculiarities = models.CharField(max_length=256, blank=True, null=True, verbose_name='Особенности')
    parking = models.CharField(max_length=256, blank=True, null=True, verbose_name='Описание парковки')
    description = models.CharField(max_length=256, blank=True, null=True, verbose_name='Описание подзала', )
    hall_no = models.IntegerField(blank=True, null=True, verbose_name="№ Зала")

    photo1 = models.ImageField(verbose_name='Фото 1', upload_to=subhall_photo_upload_to, blank=True, null=True)
    photo2 = models.ImageField(verbose_name='Фото 2', upload_to=subhall_photo_upload_to, blank=True, null=True)
    photo3 = models.ImageField(verbose_name='Фото 3', upload_to=subhall_photo_upload_to, blank=True, null=True)
    photo4 = models.ImageField(verbose_name='Фото 4', upload_to=subhall_photo_upload_to, blank=True, null=True)
    photo5 = models.ImageField(verbose_name='Фото 5', upload_to=subhall_photo_upload_to, blank=True, null=True)
    photo6 = models.ImageField(verbose_name='Фото 6', upload_to=subhall_photo_upload_to, blank=True, null=True)

    class Meta:
        verbose_name = 'Подзал'
        verbose_name_plural = 'Подзалы'

    def __str__(self):
        return self.name
