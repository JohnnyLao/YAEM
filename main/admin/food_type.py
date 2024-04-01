from django.contrib import admin

from main.models import Food_type


# @admin.register(Food_type)
# class FoodTypeAdmin(admin.ModelAdmin):
#     list_filter = ["client", "category"]
#     search_fields = ["name"]
#     list_display = ["name", "category", "z_index"]
#     list_editable = ["z_index"]
#
#     def category_name(self, obj):
#         return obj.category.name if obj.category else "Не указанно"
#
#     category_name.short_description = "Категория"
@admin.register(Food_type)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'd_name',
        'category',
        'z_index'
    )
    list_display_links = (
        'id',
        'd_name',
    )
    list_filter = ['category__client', 'category']
    search_fields = ['name']
    list_editable = ['category', 'z_index']
    fieldsets = (
        (
            'Главная информация',
            {'fields': ('name', 'category')},
        ),
        (
            'Административная информация',
            {
                'fields': (
                    'd_name',
                    'z_index',
                )
            },
        ),
    )
