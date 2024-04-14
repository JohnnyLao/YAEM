from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.utils import timezone
from main.models import City, Client


class DeliveryList(TemplateView):
    template_name = "main/delivery_list.html"

    def get_context_data(self, city_slug=None, **kwargs):
        context = super().get_context_data(**kwargs)
        city_selected = None
        # query = self.request.GET.get("q")
        clients = Client.objects.filter(status=True, delivery=True)
        # closed_clients = []
        # print(timezone.localtime(timezone.now()).time())
        # for client in clients:
        #     if timezone.localtime(timezone.now()).time() >= client.work_time_start and timezone.localtime(timezone.now()).time() <= client.work_time_end:
        #         closed_clients.append(client)
        if city_slug:
            city_selected = get_object_or_404(City, slug=city_slug)
            clients = Client.objects.filter(
                city=city_selected, status=True, delivery=True
            )
        # elif query:
        #     clients = Client.objects.filter(name__icontains=query)
        context["clients"] = clients
        context["cities"] = sorted(
            {
                client.city
                for client in Client.objects.filter(status=True, delivery=True)
                if client.city
            },
            key=lambda city: city.z_index,
        )
        context["city_selected"] = city_selected
        return context
