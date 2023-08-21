from django.contrib import admin

from main.models import City, Client, Dish, Food_type2, Category

admin.site.register(City)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ["name"]
    list_filter = ['name']


@admin.register(Food_type2)
class Food_type2Admin(admin.ModelAdmin):
    list_filter = ['category']
    search_fields = ["name"]

    def category_name(self, obj):
        return obj.category.name if obj.category else 'Не указанно'
    category_name.short_description = 'Категория'

    list_display = ["name", 'category_name']


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
