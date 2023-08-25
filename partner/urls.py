from django.urls import path
from django.views.decorators.cache import cache_page

from partner.views import Partner

cache_duration = 60 * 60 * 5
app_name = "partner"

urlpatterns = [
    path(
        "partner/", cache_page(cache_duration)(Partner.as_view()), name="partner_page"
    ),
]
