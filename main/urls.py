from django.urls import path
from main.views import Main, Menu
from django.views.decorators.cache import cache_page


# Кеширование на 5 часов
cache_duration = 0
app_name = "main"

urlpatterns = [
    path('', cache_page(cache_duration)(Main.as_view()), name="main_page"),
    path('menu/<str:url_name>/', cache_page(cache_duration)(Menu.as_view()), name="menu_page"),
]
