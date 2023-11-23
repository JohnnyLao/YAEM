from django.urls import path
from django.views.decorators.cache import cache_page

from banquets.views import BanquetList, BanquetPage
from Yaem.settings_dev import CACHES_LIFE_TIME

app_name = "cart"

urlpatterns = [
    path(
        "banquets/",
        cache_page(CACHES_LIFE_TIME)(BanquetList.as_view()),
        name="banquet_list_page",
    ),
    path(
        "<str:url_name>/banquet",
        cache_page(CACHES_LIFE_TIME)(BanquetPage.as_view()),
        name="banquet_page",
    ),
]
