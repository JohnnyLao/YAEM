from django.shortcuts import render, get_object_or_404
from django.views import View

from banquets.models import Banquet
from django.views.generic import TemplateView

from main.models import City


class BanquetList(View):
    template_name = "banquets/banquet_list.html"

    def get(self, request, *args, **kwargs):
        banquets = Banquet.objects.all()
        context = {'banquets': banquets}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        banquets = Banquet.objects.all()
        capacity = request.POST.get('capacity')
        price = request.POST.get('price_for_person')
        city = request.POST.get('city')
        if capacity:
            banquets = banquets.filter(capacity=capacity)
        if price:
            banquets = banquets.filter(price=price)
        if city:
            banquets = banquets.filter(city__name=city)
        context['banquets'] = banquets
        return render(request, self.template_name, context)


class BanquetPage(TemplateView):
    template_name = "banquets/banquet_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_name = self.kwargs['url_name']
        banquet = Banquet.objects.get(url_name=url_name)
        context['banquets'] = banquet
        return context
