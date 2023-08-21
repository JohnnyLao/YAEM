from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.translation import activate
from django.views.generic import TemplateView

from main.models import Client, Dish, Food_type2, Category


class Main(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clients"] = Client.objects.all()
        return context


class Menu(TemplateView):
    template_name = "main/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_name = self.kwargs["url_name"]
        client = Client.objects.get(url_name=url_name)
        categories = Category.objects.all()
        dishes = (
            Dish.objects.select_related("client")
            .prefetch_related("food_type")
            .filter(client=client)
        )
        # Получение уникальных категорий для блюд
        food_type = Food_type2.objects.filter(dish__in=dishes).distinct()
        context["dishes"] = dishes
        context["food_type"] = food_type
        context['categories'] = categories
        context["client"] = client
        return context


def switch_language(request):
    if request.method == "POST":
        language = request.POST.get("language")
        if language in ["ru", "en", "kk"]:
            request.session["django_language"] = language
            activate(language)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
