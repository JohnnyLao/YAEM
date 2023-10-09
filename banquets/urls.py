from django.urls import path

from banquets.views import BanquetPage

app_name = "cart"

urlpatterns = [path("banquets/", BanquetPage.as_view(), name="banquets_page")]
