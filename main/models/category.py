from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Категория")
    z_index = models.IntegerField(verbose_name="Порядковый №", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["z_index"]

    def __str__(self):
        return self.name
