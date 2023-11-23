from django.urls import path
from django.views.decorators.cache import cache_page

from partner.views import Partner
from Yaem.settings_dev import CACHES_LIFE_TIME

app_name = "partner"

urlpatterns = [
    path(
        "partner/", cache_page(CACHES_LIFE_TIME)(Partner.as_view()), name="partner_page"
    ),
]
