from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from main.models import Client, Dish


class CartPage(TemplateView):
    template_name = 'cart/cart.html'

    def get(self, request, establishment_url_name=None, *args, **kwargs):
        return render(request=request, template_name=self.template_name)
