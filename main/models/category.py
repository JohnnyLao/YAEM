from django.db import models


class Category(models.Model):
    # main info
    name = models.CharField(max_length=30, verbose_name="Категория", db_index=True)
    # to automize TODO
    client = models.ForeignKey(
        "main.Client",
        verbose_name="Клиент",
        on_delete=models.CASCADE,
        # get all establishment categories
        related_name='get_categories',
        null=True,
        blank=True,
    )
    # secondary info
    bg_image = models.ImageField(upload_to='media/temp', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Видимость')
    # admin info
    z_index = models.IntegerField(verbose_name="Порядковый №", default=1)
    d_name = models.CharField(
        max_length=50,
        verbose_name="Имя в базе",
        help_text="Алаверди_Кухня - *Auto",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        ordering = ("z_index",)

    def save(self, *args, **kwargs):
        if not self.d_name:
            if self.client and self.name:
                client_name = self.client.name.strip().lower().replace(" ", "_")
                category_name = self.name.strip().lower().replace(" ", "_")
                self.d_name = f"{client_name}_{category_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.d_name
