from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from main.models import Client


class CartPage(TemplateView):
    template_name = 'cart/cart.html'

    def get(self, request, establishment_url_name=None, *args, **kwargs):
        service_percent = Client.objects.get(url_name=establishment_url_name)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'establishment_url': establishment_url_name,
                'service_percent': service_percent.service,
                'delivery': service_percent.delivery,
            },
        )
