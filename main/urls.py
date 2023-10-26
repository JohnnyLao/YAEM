from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import Main, Menu, set_language, banquet_list, delivery_list

cache_duration = 0
app_name = "main"

urlpatterns = [
    path(
        "<str:url_name>/menu",
        cache_page(cache_duration)(Menu.as_view()),
        name="menu_page",
    ),
    path("", cache_page(cache_duration)(Main.as_view()), name="main_page"),
    path(
        "city/<slug:city_slug>/",
        cache_page(cache_duration)(Main.as_view()),
        name="city_filter",
    ),
    path("set_language/<str:language>", set_language, name="set_language"),
    path("banquet", cache_page(cache_duration)(banquet_list.as_view()), name="banquet_list_page"),
    path("delivery", cache_page(cache_duration)(delivery_list.as_view()), name="delivery_list_page")
]
