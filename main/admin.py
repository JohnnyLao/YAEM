from django.contrib import admin

from main.models import Client, City, Food_type2, Dish


admin.site.register(City)





@admin.register(Food_type2)
class Food_type2Admin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "status", "outside", "delivery", "visitors"]
    list_filter = ["city", "status"]
    search_fields = ["name"]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "food_type", "stop", "actual_price"]
    list_filter = ["food_type", "stop", "client"]
    search_fields = ["name"]
