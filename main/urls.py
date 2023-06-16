from django.urls import path
from main.views import Main, Menu, set_language, Partner, Cart

app_name = "main"

urlpatterns = [
    path('', Main.as_view(), name="main_page"),
    path('menu/<str:url_name>/', Menu.as_view(), name="menu_page"),
    # урл для работы функции переводчика
    path('set-language/', set_language, name='set_language'),
    path('partner/', Partner.as_view(), name="partner_page"),
    path('cart/', Cart.as_view(), name="cart_page")
]