from django.contrib.auth import get_user_model
from django.db import models

from main.models import Dish


class Cart(models.Model):
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь'
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

    def __str__(self):
        return f'{self.dish} ({self.quantity}) в корзине'
