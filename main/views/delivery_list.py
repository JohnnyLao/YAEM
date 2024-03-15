from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from main.models import City, Client


class DeliveryList(TemplateView):
    template_name = "main/delivery_list.html"

    def get_context_data(self, city_slug=None, **kwargs):
        context = super().get_context_data(**kwargs)
        city_selected = None
        query = self.request.GET.get("q")
        clients = Client.objects.filter(status=True).order_by("z_index")

        if city_slug:
            city_selected = get_object_or_404(City, slug=city_slug)
            clients = Client.objects.filter(city=city_selected, status=True)
        elif query:
            clients = Client.objects.filter(name__icontains=query)
        context["clients"] = clients
        context["cities"] = City.objects.all().order_by("z_index")
        context["city_selected"] = city_selected
        return context
