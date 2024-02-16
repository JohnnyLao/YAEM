from django.contrib import admin

from main.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "food_type", "stop", "actual_price", "z_index"]
    list_editable = [
        "actual_price",
    ]
    list_filter = ["client", "stop"]
    search_fields = ["name"]
