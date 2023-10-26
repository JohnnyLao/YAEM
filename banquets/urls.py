from django.urls import path

from banquets.views import BanquetPage

app_name = "cart"

urlpatterns = [
    path("banquet/", BanquetPage.as_view(), name="banquet_list_page"),
]
