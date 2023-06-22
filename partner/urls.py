from django.urls import path
from partner.views import Partner
from django.views.decorators.cache import cache_page

app_name = "partner"

urlpatterns = [
    path('partner/', cache_page(30)(Partner.as_view()), name='partner_page')
]