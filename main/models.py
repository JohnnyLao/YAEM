from django.db import models


class City(models.Model):
    name = models.CharField(max_length=40, verbose_name="Город")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")
    city = models.ForeignKey(City, models.CASCADE, verbose_name="Город")
    logo = models.ImageField(upload_to="logo", blank=True, verbose_name="Лого")
    description = models.TextField(verbose_name="Описание", max_length=60)
    working_time = models.CharField(max_length=20, verbose_name="Рабочеее время")
    address = models.CharField(max_length=50, verbose_name="Адрес")
    phone = models.DecimalField(max_digits=15, decimal_places=0, verbose_name="Телефон")
    inst = models.CharField(max_length=100, blank=True, verbose_name="Instagram")
    two_gis = models.CharField(max_length=150, verbose_name="2gis", unique=True, blank=True)
    status = models.BooleanField(verbose_name="Активен")
    outside = models.BooleanField(verbose_name="Самовывоз")
    delivery = models.BooleanField(verbose_name="Доставка")
    url_name = models.CharField(max_length=30, verbose_name="/url", unique=True)
    visitors = models.IntegerField(blank=True, default=0, verbose_name="Посетителей")
    tarif_number = models.IntegerField(blank=True, null=True, verbose_name="Тариф(1-3)")

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория')
    z_index = models.IntegerField(verbose_name='Порядковый №', blank=True, null=True, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Food_type2(models.Model):
    name = models.CharField(max_length=30, verbose_name="Подкатегория")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент', blank=True, null=True)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.name


class Dish(models.Model):
    client = models.ForeignKey(Client, models.CASCADE, verbose_name="Заведение")
    food_type = models.ForeignKey(
        Food_type2, models.CASCADE, verbose_name="Подкатегория"
    )
    name = models.CharField(verbose_name="Блюдо_RU", max_length=30)
    image = models.ImageField(verbose_name="Фото", upload_to="dishes", blank=True)
    description = models.TextField(verbose_name="Описание", max_length=100, blank=True)
    stop = models.BooleanField(verbose_name="Стоп Лист")
    old_price = models.DecimalField(
        verbose_name="Старая цена", max_digits=10, decimal_places=0, default=0
    )
    actual_price = models.DecimalField(
        verbose_name="Текущая цена", max_digits=10, decimal_places=0
    )

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return self.name
