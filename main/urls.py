from django.urls import path
from main.views import Main, Menu
from django.views.decorators.cache import cache_page

app_name = "main"

urlpatterns = [
    path('', cache_page(1)(Main.as_view()), name="main_page"),
    path('menu/<str:url_name>/', cache_page(1)(Menu.as_view()), name="menu_page"),


]