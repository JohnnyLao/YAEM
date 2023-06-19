from django.views.generic import TemplateView

from main.models import Dish, Client


class Partner(TemplateView):
    template_name = 'partner/partner.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_dishes'] = Dish.objects.count()
        context['total_clients'] = Client.objects.count()
        context["total_orders"] = (context['total_dishes'] * 21)
        return context
