from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import TemplateView

from banquets.models import BanquetCard
from main.models import City


class BanquetList(View):
    template_name = "banquets/banquet_list.html"

    def get(self, request, *args, **kwargs):
        banquets = BanquetCard.objects.all().order_by("z_index")
        cities = City.objects.values_list("name", flat=True).distinct()
        capacity = request.GET.get("capacity")
        price_min_max = request.GET.get("price_min_max")
        city = request.GET.get("city")

        if capacity:
            if capacity == "100":
                banquets = banquets.filter(capacity__lte=100)
            elif capacity == "200":
                banquets = banquets.filter(capacity__gte=100, capacity__lte=200)
            elif capacity == "400":
                banquets = banquets.filter(capacity__gte=200, capacity__lte=400)
            elif capacity == "401":
                banquets = banquets.filter(capacity__gte=401)

        if price_min_max:
            if price_min_max == "3000":
                banquets = banquets.filter(price_min__gte=0, price_min__lte=3000)
            elif price_min_max == "5000":
                banquets = banquets.filter(price_min__gte=3000, price_min__lte=5000)
            elif price_min_max == "10000":
                banquets = banquets.filter(price_min__gte=5000, price_min__lte=10000)
            elif price_min_max == "10001":
                banquets = banquets.filter(price_min__gte=10001)

        if city:
            if city == "Temirtau" or city == "Темиртау" or city == "Теміртау":
                banquets = banquets.filter(
                    Q(city__name="Temirtau")
                    | Q(city__name="Темиртау")
                    | Q(city__name="Теміртау")
                )
            elif city == "Karaganda" or city == "Караганда" or city == "Қарағанды":
                banquets = banquets.filter(
                    Q(city__name="Karaganda")
                    | Q(city__name="Караганда")
                    | Q(city__name="Қарағанды")
                )
            elif city == "Almaty" or city == "Алматы" or city == "Алматы":
                banquets = banquets.filter(
                    Q(city__name="Almaty")
                    | Q(city__name="Алматы")
                    | Q(city__name="Алматы")
            )
            elif city == "Astana" or city == "Астана" or city == "Астана":
                banquets = banquets.filter(
                    Q(city__name="Astana")
                    | Q(city__name="Астана")
                    | Q(city__name="Астана")
            )

        context = {"banquets": banquets, "cities": cities}
        return render(request, self.template_name, context)


class BanquetPage(TemplateView):
    template_name = "banquets/banquet_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_name = self.kwargs["url_name"]
        banquet_card = BanquetCard.objects.get(url_name=url_name)
        subhall = banquet_card.banquet_set.all()
        context["banquet"] = banquet_card
        context["subhall"] = subhall
        return context
