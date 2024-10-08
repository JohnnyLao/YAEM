from django.urls import path
from django.views.decorators.cache import cache_page

from banquets.views import BanquetList, BanquetPage
from Yaem.settings import CACHES_LIFE_TIME

app_name = "banquets"

urlpatterns = [
    path(
        "banquets/",
        cache_page(CACHES_LIFE_TIME)(BanquetList.as_view()),
        name="banquet_list_page",
    ),
    path(
        "banquet/<str:url_name>",
        cache_page(CACHES_LIFE_TIME)(BanquetPage.as_view()),
        name="banquet_page",
    ),
]
