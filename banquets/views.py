from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View

from banquets.models import Banquet
from django.views.generic import TemplateView

from main.models import City


class BanquetList(View):
    template_name = "banquets/banquet_list.html"

    def get(self, request, *args, **kwargs):
        banquets = Banquet.objects.all()
        cities = City.objects.values_list('name', flat=True).distinct()
        capacity = request.GET.get('capacity')
        price_min_max = request.GET.get('price_min_max')
        city = request.GET.get('city')

        if capacity:
            if capacity == '100':
                banquets = Banquet.objects.filter(capacity__lte=100)
            elif capacity == '200':
                banquets = Banquet.objects.filter(capacity__gte=100, capacity__lte=200)
            elif capacity == '400':
                banquets = Banquet.objects.filter(capacity__gte=200, capacity__lte=400)
            elif capacity == '401':
                banquets = Banquet.objects.filter(capacity__gte=401)

        if price_min_max:
            if price_min_max == '3000':
                banquets = Banquet.objects.filter(price_min__gte=0, price_min__lte=3000)
            elif price_min_max == '5000':
                banquets = Banquet.objects.filter(price_min__gte=3000, price_min__lte=5000)
            elif price_min_max == '10000':
                banquets = Banquet.objects.filter(price_min__gte=5000, price_min__lte=10000)
            elif price_min_max == '15000':
                banquets = Banquet.objects.filter(price_min__gte=10000, price_min__lte=15000)

        if city:
            if city == 'Temirtau' or city == 'Темиртау' or city == 'Теміртау':
                banquets = banquets.filter(Q(city__name='Temirtau') | Q(city__name='Темиртау') | Q(city__name='Теміртау'))
            elif city == 'Karaganda' or city == 'Караганда' or city == 'Қарағанды':
                 banquets = banquets.filter(Q(city__name='Karaganda') | Q(city__name='Караганда') | Q(city__name='Қарағанды'))




        context = {
            'banquets': banquets,
            'cities': cities
        }
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     context = {}
    #     banquets = Banquet.objects.all()
    #     capacity = request.POST.get('capacity')
    #     price = request.POST.get('price_for_person')
    #     city = request.POST.get('city')
    #     if capacity:
    #         banquets = banquets.filter(capacity=capacity)
    #     if price:
    #         banquets = banquets.filter(price=price)
    #     if city:
    #         banquets = banquets.filter(city__name=city)
    #     context['banquets'] = banquets
    #     return render(request, self.template_name, context)


class BanquetPage(TemplateView):
    template_name = "banquets/banquet_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_name = self.kwargs['url_name']
        banquet = Banquet.objects.get(url_name=url_name)
        context['banquets'] = banquet
        return context
