from crum import get_current_user
from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from main.models.utils.choices import PaymentStatuses


class Payment(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
        verbose_name='Пользователь',
        related_name='get_user_payments',
    )
    tarif_number = models.ForeignKey(
        "main.EstablishmentRates",
        on_delete=models.CASCADE,
        verbose_name="Тариф",
    )
    months = models.PositiveSmallIntegerField(verbose_name='Количество месяцев')
    phone = PhoneNumberField(verbose_name='Номер телефона')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания заявки'
    )
    status = models.CharField(
        choices=PaymentStatuses.choices, max_length=20, verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Заявки на оплату'
        verbose_name_plural = 'Заявки на оплату'
        ordering = ('created_at',)

    def save(self, *args, **kwargs):
        # Create relation with current user
        if not self.user_id:
            self.user = get_current_user()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.status
