from django.contrib import admin

from main.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "food_type", "stop", "actual_price", "z_index"]
    list_editable = [
        "actual_price", "z_index"
    ]
    list_filter = ["client", "food_type","stop"]
    search_fields = ["name"]
