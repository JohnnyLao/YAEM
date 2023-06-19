from django.urls import path
from .views import AddToCartView, CartView

app_name = 'cart'

urlpatterns = [
    # URL-шаблон для добавления товара в корзину
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),

    # URL-шаблон для отображения содержимого корзины
    path('cart/', CartView.as_view(), name='cart_page'),
]
