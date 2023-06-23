from django.shortcuts import redirect
from django.views.generic import TemplateView
from main.models import Client, Dish, Food_type2, Client_Type
from django.utils.translation import activate



class Main(TemplateView):
    template_name = "main/index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clients"] = Client.objects.values('name',
                                                   'working_time',
                                                   'description',
                                                   'status',
                                                   'delivery',
                                                   'url_name',
                                                   'logo')
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
        context['client'] = client

        return context
