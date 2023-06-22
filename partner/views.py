from django.views.generic import TemplateView

from main.models import Dish, Client


class Partner(TemplateView):
    template_name = 'partner/partner.html'


