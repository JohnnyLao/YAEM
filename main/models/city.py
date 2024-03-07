from django.db import models


class City(models.Model):
    name = models.CharField(max_length=40, verbose_name="Город")
    slug = models.SlugField(unique=True, verbose_name="Слаг", blank=True, null=True)
    z_index = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name
