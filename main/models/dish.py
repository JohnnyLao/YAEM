from django.db import models

from main.models.utils.images_upload import dish_image_upload_to


class Dish(models.Model):
    # main info
    # remove
    client = models.ForeignKey(
        "main.Client",
        models.CASCADE,
        verbose_name="Заведение",
        help_text="Блюдо какого заведения",
    )
    food_type = models.ForeignKey(
        "main.Food_type",
        models.CASCADE,
        verbose_name="Подкатегория",
        help_text="Подкатегория",
    )
    name = models.CharField(
        verbose_name="Блюдо", max_length=40, help_text="Наименование (40 символов)"
    )
    actual_price = models.DecimalField(
        verbose_name="Текущая цена", max_digits=10, decimal_places=0
    )
    stop = models.BooleanField(verbose_name="Стоп Лист", default=False)
    # secondary info
    image = models.ImageField(
        verbose_name="Фото", upload_to=dish_image_upload_to, blank=True, null=True
    )
    description = models.TextField(
        verbose_name="Описание",
        max_length=120,
        blank=True,
        help_text="Описание блюда (120 символов)",
    )
    old_price = models.DecimalField(
        verbose_name="Старая цена",
        max_digits=10,
        decimal_places=0,
        default=0,
        help_text="Если старая цена выше актуальной, будет отражена скидка",
    )
    popular = models.BooleanField(
        verbose_name="Популярное", default=False, help_text="Значок популярно"
    )
    spicy = models.BooleanField(
        verbose_name="Острое", default=False, help_text="Значок остроты"
    )
    vegetarian = models.BooleanField(
        verbose_name="Вегетарианское", default=False, help_text="Значок вегетарианское"
    )
    # admin info
    generated = models.BooleanField(
        verbose_name="Фото сгенерировано",
        default=False,
        help_text="Предупреждение о генерации",
    )
    z_index = models.IntegerField(
        verbose_name="Порядковый №",
        blank=True,
        null=True,
        help_text="Порядок отображения 0-99",
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Время создания', null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Время обновления', null=True)


    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ("z_index",)

    # get total price
    def total_price(self):
        if self.old_price:
            return self.old_price
        return self.actual_price

    # get total price service
    def total_price_with_service(self):
        if self.client.service > 0:
            if self.old_price:
                return self.old_price + (self.old_price * self.client.service / 100)
            else:
                return self.actual_price + (
                    self.actual_price * self.client.service / 100
                )
        return self.total_price()

    def __str__(self):
        return self.name
