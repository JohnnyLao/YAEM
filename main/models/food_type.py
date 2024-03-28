from django.db import models


class Food_type(models.Model):
    # main info
    # remove
    client = models.ForeignKey(
        "main.Client", verbose_name="Клиент", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(
        max_length=50, verbose_name="Отображаемое имя", help_text="Супы", db_index=True,
    )
    # to automize #TODO
    category = models.ForeignKey(
        "main.Category",
        on_delete=models.CASCADE,
        verbose_name="Категория",
        blank=True,
        null=True,
        db_index=True,
    )
    # admin info
    z_index = models.IntegerField(
        verbose_name="Порядковый №",
        default=0,
        help_text="Категория",
    )
    d_name = models.CharField(
        max_length=50,
        verbose_name="Имя в базе",
        help_text="Супы_Алаверди",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ('z_index',)

    def __str__(self):
        return self.d_name
