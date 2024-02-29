from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to='users.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='profile',
        primary_key=True,
        db_index=True,
    )
    telegram_id = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='Телеграм ID'
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'
        ordering = ('user',)
