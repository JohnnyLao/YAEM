from django.db import models


class KitchenType(models.Model):
    kitchen_type = models.CharField(max_length=256, verbose_name="Вид кухни")

    class Meta:
        verbose_name = "Вид кухни"
        verbose_name_plural = "Виды кухни"

    def __str__(self):
        return self.kitchen_type
