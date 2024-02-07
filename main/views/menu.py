from django.views.generic import TemplateView

from banquets.models import BanquetCard
from main.models import Category, Client, Dish, Food_type


class Menu(TemplateView):
    template_name = "main/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_name = self.kwargs["url_name"]
        client = Client.objects.get(url_name=url_name)
        categories = Category.objects.all().order_by("z_index")
        client_has_banquet = BanquetCard.objects.filter(client=client).exists()
        dishes = (
            Dish.objects.select_related("client")
            .prefetch_related("food_type")
            .filter(client=client)
            .order_by("z_index")
        )
        # Получение уникальных категорий для блюд
        food_type = (
            Food_type.objects.filter(dish__in=dishes).distinct().order_by("z_index")
        )
        context["dishes"] = dishes
        context["food_type"] = food_type
        context["categories"] = categories
        context["client"] = client
        context["client_has_banquet"] = client_has_banquet

        return context
