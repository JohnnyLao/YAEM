from django.db import models


class Category(models.Model):
    # main info
    name = models.CharField(max_length=30, verbose_name="Категория", db_index=True)
    # to automize TODO
    client = models.ForeignKey(
        "main.Client", verbose_name="Клиент", on_delete=models.SET_NULL, null=True, blank=True
    )
    # secondary info
    bg_image = models.ImageField(upload_to='media/temp', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Видимость')
    # admin info
    z_index = models.IntegerField(verbose_name="Порядковый №", default=1)
    d_name = models.CharField(
        max_length=50,
        verbose_name="Имя в базе",
        help_text="Кухня_Алаверди",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("z_index",)

    def __str__(self):
        return self.name
