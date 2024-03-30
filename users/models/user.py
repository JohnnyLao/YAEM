from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.models.user_manager import CustomUserManager


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    phone_number = PhoneNumberField(
        verbose_name='Номер телефона', unique=True, db_index=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name='Создан', null=True
    )

    USERNAME_FIELD = 'phone_number'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('created_at',)

    def __str__(self):
        if self.is_superuser or self.is_staff:
            if self.first_name:
                return f'{self.phone_number}({self.first_name})'
            return f'{self.phone_number}'
        return f'{self.phone_number}'
