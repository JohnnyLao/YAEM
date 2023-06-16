from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from main.models import Client, Dish, Food_type2, Client_Type
from django.utils.translation import activate


class Main(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clients"] = Client.objects.all()
        context["types"] = Client_Type.objects.all()
        return context


class Menu(TemplateView):
    template_name = "main/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_name = self.kwargs['url_name']
        client = Client.objects.get(url_name=url_name)
        dishes = Dish.objects.filter(client=client)
        # Получение уникальных категорий для блюд
        food_type = Food_type2.objects.filter(dish__in=dishes).distinct()
        context['dishes'] = dishes
        context['food_type'] = food_type
        return context


class Partner(TemplateView):
    template_name = "main/partner.html"


class Cart(TemplateView):
    template_name = "main/cart.html"

# Перевод шаблонов на разные языки
def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')  # получил выбранный язык из запроса
        request.session['django_language'] = language  # сохранил выбранный язык в сессии
        activate(language)  # установил выбранный язык
    return redirect(request.META.get('HTTP_REFERER', '/'))
