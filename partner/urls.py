from django.urls import path
from partner.views import Partner
from django.views.decorators.cache import cache_page



cache_duration = 5 * 60 * 60  # 5 часов * 60 минут * 60 секунд
app_name = "partner"

urlpatterns = [
    path('partner/', (Partner.as_view()), name='partner_page')
]
