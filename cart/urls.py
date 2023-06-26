from django.urls import path
from cart.views import CartView, AddToCartView, CartClearView

app_name = 'cart'

urlpatterns = [
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),

    path('cart/', CartView.as_view(), name='cart_page'),

    path('cart/clear/', CartClearView.as_view(), name='cart_clear'),

]
