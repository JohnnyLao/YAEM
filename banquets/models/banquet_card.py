from django.db import models

from banquets.models.utils.images_upload import banquet_logo_upload_to


class BanquetCard(models.Model):
    client = models.ForeignKey(
        to="main.Client",
        verbose_name="Зал заведения:",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    city = models.ForeignKey("main.City", models.CASCADE, verbose_name="Город")
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
        ordering = ("-z_index",)

    def __str__(self):
        return self.name
