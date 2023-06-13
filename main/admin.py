from django.contrib import admin
from main.models import *

admin.site.register(Client_Type)
admin.site.register(City)
admin.site.register(Client_Category)


@admin.register(Food_type)
class Food_typeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ["client"]


@admin.register(Food_type2)
class Food_type2Admin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', "status", "outside", "delivery", "visitors"]
    list_filter = ["city", "status"]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', "food_type", "stop", "actual_price"]
    list_filter = ["food_type", "stop", "client"]
