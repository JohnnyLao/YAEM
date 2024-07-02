from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from main.models import Client


class CartPage(TemplateView):
    template_name = 'cart/cart.html'

    def get(self, request, establishment_url_name=None, *args, **kwargs):
        client = get_object_or_404(Client, url_name=establishment_url_name)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'establishment_url': establishment_url_name,
                'service_percent': client.service,
                'delivery': client.delivery,
                'outside': client.outside,
                'phone': client.phone,
                'delivery_description': client.delivery_description,
            },
        )
