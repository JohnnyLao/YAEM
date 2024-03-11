from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from users.models.user_manager import CustomUserManager


class User(AbstractUser):
    username = models.CharField(
        verbose_name="Никнейм",
        max_length=64,
        blank=True,
        default='',
    )
    email = models.EmailField("Почта", unique=True, blank=True)
    phone_number = PhoneNumberField(
        verbose_name='Номер телефона', unique=True, db_index=True
    )
    is_corporate = models.BooleanField(
        verbose_name='Корпоративный аккаунт', default=False
    )

    USERNAME_FIELD = 'phone_number'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.first_name


@receiver(signal=post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not hasattr(User, 'profile') and not created:
        from users.models import Profile

        Profile.objects.create(user=instance)
