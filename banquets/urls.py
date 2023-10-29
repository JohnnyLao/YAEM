from django.urls import path

from banquets.views import BanquetList, BanquetPage

app_name = "cart"

urlpatterns = [
    path("banquets/", BanquetList.as_view(), name="banquet_list_page"),
    path('<str:url_name>/banquet', BanquetPage.as_view(), name='banquet_page')
]
