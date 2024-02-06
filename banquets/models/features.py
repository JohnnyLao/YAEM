from django.db import models


class FeaturesOfTheBanquetHall(models.Model):
    features_name = models.CharField(
        max_length=256, verbose_name="Особенности банкетного зала"
    )

    class Meta:
        verbose_name = "Особенность банкетного зала"
        verbose_name_plural = "Особенности банкетных залов"

    def __str__(self):
        return self.features_name
