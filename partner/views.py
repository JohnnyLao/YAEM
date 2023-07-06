from django.views.generic import TemplateView

from main.models import Client, Dish


class Partner(TemplateView):
    template_name = "partner/partner.html"
