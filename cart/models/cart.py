import math

from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_out
from django.contrib.sessions.models import Session
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from main.models import Dish


class Cart(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        null=True,
    )
    items = models.ManyToManyField(
        to=Dish, through='CartItems', verbose_name='Блюда в корзине'
    )
    session_key = models.CharField(
        max_length=32, null=True, blank=True, verbose_name='Сессионный ключ'
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания корзины'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def total_cost(self):
        return sum(item.subtotal() for item in self.cart_items.all())

    def total_cost_with_service(self):
        return math.ceil(sum(item.subtotal_with_service() for item in self.cart_items.all()))

    def __str__(self):
        return f'{self.user}'


class CartItems(models.Model):
    cart = models.ForeignKey(
        to=Cart,
        on_delete=models.CASCADE,
        verbose_name='Корзина',
        related_name='cart_items',
    )
    dish = models.ForeignKey(to=Dish, on_delete=models.CASCADE, verbose_name='Блюдо')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'

    def subtotal(self):
        return self.dish.total_price() * self.quantity

    def subtotal_with_service(self):
        return self.dish.total_price_with_service() * self.quantity

    def __str__(self):
        return f'{self.dish} ({self.quantity}) в корзине'


@receiver(pre_delete, sender=Session)
def delete_anonim_session_cart(sender, instance, **kwargs):
    session_key = instance.session_key
    anonim_cart = Cart.objects.filter(session_key=session_key).first()
    if anonim_cart:
        anonim_cart.delete()


@receiver(user_logged_out)
def delete_user_cart_on_logout(sender, user, request, **kwargs):
    if user.is_authenticated:
        user_cart = Cart.objects.filter(user=user).first()
        if user_cart:
            user_cart.delete()
