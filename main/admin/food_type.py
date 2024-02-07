from django.contrib import admin

from main.models import Food_type


@admin.register(Food_type)
class FoodTypeAdmin(admin.ModelAdmin):
    list_filter = ["client"]
    search_fields = ["name"]
    filter_horizontal = ["client"]
    list_display = ["name", "category_name", "z_index"]

    def category_name(self, obj):
        return obj.category.name if obj.category else "Не указанно"

    category_name.short_description = "Категория"
