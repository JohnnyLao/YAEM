from django.db import models


class Food_type(models.Model):
    # main info
    name = models.CharField(
        max_length=50,
        verbose_name="Отображаемое имя",
        help_text="Супы",
        db_index=True,
    )
    # to automize #TODO
    category = models.ForeignKey(
        "main.Category",
        on_delete=models.CASCADE,
        verbose_name="Раздел",
        # get all subcategories
        related_name='get_subcategories',
        blank=True,
        null=True,
        db_index=True,
    )
    # admin info
    z_index = models.IntegerField(
        verbose_name="Порядковый №",
        default=0,
        help_text="Раздел",
    )
    d_name = models.CharField(
        max_length=50,
        verbose_name="Имя в базе",
        help_text="Супы_Алаверди",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('z_index',)

    def save(self, *args, **kwargs):
        if not self.d_name:
            if self.category and self.name:
                category_d_name = self.category.d_name if self.category.d_name else ""
                subcategory_name = self.name.strip().lower().replace(" ", "_")
                self.d_name = f"{category_d_name}_{subcategory_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.d_name
