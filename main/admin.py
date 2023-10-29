from django.contrib import admin
from main.models import Category, City, Client, Dish, Food_type2, EstablishmentRates

admin.site.site_header = "Yaem"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "z_index"]
    search_fields = ["name"]
    list_filter = ["name"]


@admin.register(Food_type2)
class Food_type2Admin(admin.ModelAdmin):
    list_filter = ["client"]
    search_fields = ["name"]
    filter_horizontal = ["client"]

    def category_name(self, obj):
        return obj.category.name if obj.category else "Не указанно"

    category_name.short_description = "Категория"

    list_display = ["name", "category_name", "z_index"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "status", "outside", "delivery"]
    list_filter = ["city", "status"]
    search_fields = ["name"]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "food_type", "stop", "actual_price", "z_index"]
    list_filter = ["client", "stop"]
    search_fields = ["name"]


@admin.register(EstablishmentRates)
class EstablishmentRatesAdmin(admin.ModelAdmin):
    pass
