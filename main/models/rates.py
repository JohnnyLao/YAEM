from django.db import models

from main.models.utils.choices import Rates


class EstablishmentRates(models.Model):
    name = models.CharField(
        max_length=15,
        choices=Rates.choices,
        verbose_name="Название тарифа",
        unique=True,
        editable=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"
        ordering = ('id',)
