from django.urls import path
from django.views.decorators.cache import cache_page
from main.views import Main, Menu


cache_duration = 0
app_name = "main"

urlpatterns = [
    path(
        "<str:url_name>/menu",
        cache_page(cache_duration)(Menu.as_view()),
        name="menu_page",
    ),
    path("", cache_page(cache_duration)(Main.as_view()), name="main_page"),
]
