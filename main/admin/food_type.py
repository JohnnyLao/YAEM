from django.contrib import admin

from main.models import Food_type


@admin.register(Food_type)
class FoodTypeAdmin(admin.ModelAdmin):
    list_filter = ["client", "category"]
    search_fields = ["name"]
    list_display = ["name", "category", "z_index"]
    list_editable = ["z_index"]

    def category_name(self, obj):
        return obj.category.name if obj.category else "Не указанно"

    category_name.short_description = "Категория"
