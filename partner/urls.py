from django.urls import path
from partner.views import Partner

app_name = "partner"

urlpatterns = [
    path('partner', Partner.as_view(), name='partner_page')
]