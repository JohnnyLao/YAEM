from django.db import models

from main.models.utils.images_upload import dish_image_upload_to


class Dish(models.Model):
    client = models.ForeignKey("main.Client", models.CASCADE, verbose_name="Заведение")
    food_type = models.ForeignKey(
        "main.Food_type", models.CASCADE, verbose_name="Подкатегория"
    )
    name = models.CharField(verbose_name="Блюдо_RU", max_length=30)
    image = models.ImageField(
        verbose_name="Фото", upload_to=dish_image_upload_to, blank=True, null=True
    )
    generated = models.BooleanField(verbose_name="Фото сгенерировано", default=0)
    popular = models.BooleanField(verbose_name="Популярное (знак)", default=0)
    spicy = models.BooleanField(verbose_name="Острое (знак)", default=0)
    vegetarian = models.BooleanField(verbose_name="Вегетерианское (знак)", default=0)
    description = models.TextField(verbose_name="Описание", max_length=100, blank=True)
    stop = models.BooleanField(verbose_name="Стоп Лист")
    old_price = models.DecimalField(
        verbose_name="Старая цена", max_digits=10, decimal_places=0, default=0
    )
    actual_price = models.DecimalField(
        verbose_name="Текущая цена", max_digits=10, decimal_places=0
    )
    z_index = models.IntegerField(verbose_name="Порядковый №", blank=True, null=True)

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ["z_index"]

    def __str__(self):
        return self.name
