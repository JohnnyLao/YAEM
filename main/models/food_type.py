from django.db import models


class Food_type(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Отображаемое имя", help_text="Супы"
    )
    d_name = models.CharField(
        max_length=50,
        verbose_name="Имя в базе",
        help_text="Супы_Алаверди",
        default="CATEGORY",
    )
    category = models.ForeignKey(
        "main.Category",
        on_delete=models.CASCADE,
        verbose_name="Категория",
        blank=True,
        null=True,
    )
    client = models.ForeignKey(
        "main.Client", verbose_name="Клиент", on_delete=models.SET_NULL, null=True
    )
    z_index = models.IntegerField(
        verbose_name="Порядковый №",
        default=0,
        help_text="Акции: 0, "
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
        "Разное: 101-110",
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.d_name
