from django.db import models
import os


class City(models.Model):
    name = models.CharField(max_length=40, verbose_name="Город")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


def get_logo_upload_path(instance, filename):
    return f"./static/images/{instance.url_name}/logo/{filename}"


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")
    city = models.ForeignKey(City, models.CASCADE, verbose_name="Город")
    logo = models.ImageField(upload_to=get_logo_upload_path, blank=True, verbose_name="Лого")
    description = models.TextField(verbose_name="Описание", max_length=60)
    working_time = models.CharField(max_length=20, verbose_name="Рабочеее время")
    address = models.CharField(max_length=50, verbose_name="Адрес")
    phone = models.DecimalField(max_digits=15, decimal_places=0, verbose_name="Телефон")
    inst = models.CharField(max_length=100, blank=True, verbose_name="Instagram")
    status = models.BooleanField(verbose_name="Активен")
    outside = models.BooleanField(verbose_name="Самовывоз")
    delivery = models.BooleanField(verbose_name="Доставка")
    url_name = models.CharField(max_length=30, verbose_name="/url", unique=True)
    visitors = models.IntegerField(blank=True, default=0, verbose_name="Посетителей")

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Создаем папку для хранения логотипов при сохранении экземпляра класса
        if not self.pk:
            os.makedirs(f"./static/images/{self.name}/logo/", exist_ok=True)
        super().save(*args, **kwargs)


class Client_Type(models.Model):
    name = models.CharField(max_length=50, verbose_name="Область")

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"

    def __str__(self):
        return self.name


class Client_Category(models.Model):
    client = models.ForeignKey(Client, models.CASCADE, verbose_name="Заведение")
    category = models.ForeignKey(Client_Type, models.CASCADE, verbose_name="Область")

    class Meta:
        verbose_name = "Заведение-Область"
        verbose_name_plural = "Заведение - Области"

    def __str__(self):
        return f'В {self.client} есть {self.category}'


class Food_type(models.Model):
    name = models.CharField(max_length=30, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Food_type2(models.Model):
    name = models.CharField(max_length=30, verbose_name="Подкатегория")
    category = models.ForeignKey(Food_type, models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.name


def get_dish_upload_path(instance, filename):
    return f"./static/images/{instance.client.url_name}/dishes/{filename}"


class Dish(models.Model):
    client = models.ForeignKey(Client, models.CASCADE, verbose_name="Заведение")
    food_type = models.ForeignKey(Food_type2, models.CASCADE, verbose_name="Подкатегория")
    name = models.CharField(verbose_name="Блюдо_RU", max_length=30)
    name_kz = models.CharField(verbose_name="Блюдо_KZ", max_length=50, blank=True)
    name_en = models.CharField(verbose_name="Блюдо_EN", max_length=50, blank=True)
    image = models.ImageField(verbose_name="Фото", upload_to=get_dish_upload_path, blank=True)
    description = models.TextField(verbose_name="Описание", max_length=100, blank=True)
    stop = models.BooleanField(verbose_name="Стоп Лист")
    old_price = models.DecimalField(verbose_name="Старая цена",max_digits=10, decimal_places=0, default=0)
    actual_price = models.DecimalField(verbose_name="Текущая цена", max_digits=10, decimal_places=0)

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return self.name
