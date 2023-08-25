from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import activate
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from main.models import Category, City, Client, Dish, Food_type2


class Main(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, city_slug=None, **kwargs):
        context = super().get_context_data(**kwargs)
        city_selected = None
        if city_slug:
            # city = City.objects.get(slug=city_slug)
            city_selected = get_object_or_404(City, slug=city_slug)
            context["clients"] = Client.objects.filter(city=city_selected)
        else:
            context["clients"] = Client.objects.all()
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
        return context


def switch_language(request):
    if request.method == "POST":
        language = request.POST.get("language")
        if language in ["ru", "en", "kk"]:
            request.session["django_language"] = language
            activate(language)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
