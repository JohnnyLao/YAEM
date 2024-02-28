from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from users.models.user_manager import CustomUserManager


class User(AbstractUser):
    phone_number = PhoneNumberField(verbose_name='Номер телефона', unique=True)

    USERNAME_FIELD = 'phone_number'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return f'{self.first_name} - Фамилия не указана'
        elif self.last_name:
            return f'Имя не указано - {self.last_name}'
        else:
            return 'Личные данные не указанны'

    def __str__(self):
        return self.full_name
