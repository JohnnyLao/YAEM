from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Категория")
    z_index = models.IntegerField(verbose_name="Порядковый №", blank=True, null=True)
    client = models.ForeignKey(
        "main.Client", verbose_name="Клиент", on_delete=models.SET_NULL, null=True
    )
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
        ordering = ["z_index"]

    def __str__(self):
        return self.name
