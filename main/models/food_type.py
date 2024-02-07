from django.db import models


class Food_type(models.Model):
    name = models.CharField(max_length=30, verbose_name="Подкатегория")
    category = models.ForeignKey(
        "main.Category",
        on_delete=models.CASCADE,
        verbose_name="Категория",
        blank=True,
        null=True,
    )
    client = models.ManyToManyField("main.Client", verbose_name="Клиент")
    z_index = models.IntegerField(verbose_name="Порядковый №", default=0)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.name
