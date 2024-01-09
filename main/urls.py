from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import DeliveryList, Main, Menu, set_language
from Yaem.settings import CACHES_LIFE_TIME

app_name = "main"

urlpatterns = [
    path(
        "<str:url_name>/menu",
        cache_page(CACHES_LIFE_TIME)(Menu.as_view()),
        name="menu_page",
    ),
    path("", cache_page(CACHES_LIFE_TIME)(Main.as_view()), name="main_page"),
    path("delivery/city/<slug:city_slug>/", DeliveryList.as_view(), name="city_filter"),
    path("set_language/<str:language>", set_language, name="set_language"),
    path(
        "delivery/",
        cache_page(CACHES_LIFE_TIME)(DeliveryList.as_view()),
        name="delivery_list_page",
    ),
]
