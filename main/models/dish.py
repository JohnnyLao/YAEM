from django.db import models

from main.models.utils.images_upload import dish_image_upload_to


class Dish(models.Model):
    client = models.ForeignKey("main.Client", models.CASCADE, verbose_name="Заведение", help_text="Блюдо какого заведения")
    food_type = models.ForeignKey(
        "main.Food_type", models.CASCADE, verbose_name="Подкатегория", help_text="Подкатегория"
    )
    name = models.CharField(verbose_name="Блюдо", max_length=40, help_text="Наименование (40 символов)")
    image = models.ImageField(
        verbose_name="Фото", upload_to=dish_image_upload_to, blank=True, null=True
    )
    generated = models.BooleanField(verbose_name="Фото сгенерировано", default=False, help_text="Предупреждение о генерации")
    description = models.TextField(verbose_name="Описание", max_length=120, blank=True, help_text="Описание блюда (120 символов)")
    popular = models.BooleanField(verbose_name="Популярное", default=False, help_text="Значок популярно")
    spicy = models.BooleanField(verbose_name="Острое", default=False, help_text="Значок остроты")
    vegetarian = models.BooleanField(verbose_name="Вегетарианское", default=False, help_text="Значок вегетарианское")
    stop = models.BooleanField(verbose_name="Стоп Лист")
    old_price = models.DecimalField(
        verbose_name="Старая цена", max_digits=10, decimal_places=0, default=0, help_text="Если старая цена выше актуальной, будет отражена скидка")
    actual_price = models.DecimalField(
        verbose_name="Текущая цена", max_digits=10, decimal_places=0
    )
    z_index = models.IntegerField(verbose_name="Порядковый №", blank=True, null=True, help_text="Акции: 0, "
                                                                                                "Популярные: 1, "
                                                                                                "Закуски: 2-10, "
                                                                                                "Салаты: 11-20, "
                                                                                                "Супы: 21-30, "
                                                                                                "Основные: 31-40, "
                                                                                                "Пиццы: 41-45, "
                                                                                                "Шашлыки: 46-50, "
                                                                                                "Десерты: 51-60, "
                                                                                                "Безалкагольное: 61-70, "
                                                                                                "Алкаголь: 71-100, "
                                                                                                "Разное: 101-110")

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ["z_index"]

    def __str__(self):
        return self.name
