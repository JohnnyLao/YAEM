from urllib.parse import urlparse

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.views.generic import TemplateView

from banquets.models import BanquetCard
from main.models import Category, City, Client, Dish, Food_type2

from django.core.cache import cache


class Main(TemplateView):
    template_name = "main/index.html"


class DeliveryList(TemplateView):
    template_name = "main/delivery_list.html"

    def get_context_data(self, city_slug=None, **kwargs):
        context = super().get_context_data(**kwargs)
        city_selected = None
        query = self.request.GET.get("q")
        clients = Client.objects.all()

        if city_slug:
            city_selected = get_object_or_404(City, slug=city_slug)
            clients = Client.objects.filter(city=city_selected)
        elif query:
            clients = Client.objects.filter(name__icontains=query)
        context["clients"] = clients
        context["cities"] = City.objects.all()
        context["city_selected"] = city_selected
        return context


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
            Food_type2.objects.filter(dish__in=dishes).distinct().order_by("z_index")
        )
        context["dishes"] = dishes
        context["food_type"] = food_type
        context["categories"] = categories
        context["client"] = client
        context['client_has_banquet'] = client_has_banquet

        return context


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(
            f"{view.namespace}:{view.url_name}", args=view.args, kwargs=view.kwargs
        )
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
