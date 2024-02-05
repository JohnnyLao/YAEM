from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views import View

from banquets.models import BanquetCard
from banquets.views import utils
from main.models import City


class BanquetList(View):
    template_name = "banquets/banquet_list.html"

    def get(self, request, *args, **kwargs):
        banquets = BanquetCard.objects.all().order_by("z_index")
        cities = City.objects.values_list("name", flat=True).distinct()
        capacity = request.GET.get("capacity")
        price_min_max = request.GET.get("price_min_max")
        city = request.GET.get("city")

        def apply_filter(queryset, field, values):
            q_objects = Q()
            for value in values:
                q_objects |= Q(**{field: value})
            return queryset.filter(q_objects)

        if capacity:
            banquets = banquets.filter(
                capacity__range=utils.capacity_ranges.get(capacity, (0, 9999))
            )

        if price_min_max:
            banquets = banquets.filter(
                price_min__range=utils.price_ranges.get(price_min_max, (0, 99999))
            )

        if city:
            for city_name, city_synonym_list in utils.city_synonyms.items():
                if city in city_synonym_list:
                    banquets = apply_filter(banquets, "city__name", city_synonym_list)

        context = {"banquets": banquets, "cities": cities}
        return render(request, self.template_name, context)
