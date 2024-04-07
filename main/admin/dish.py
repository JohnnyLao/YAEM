from django.contrib import admin

from main.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    list_display = (
        'id',
        'name',
        'get_client_name',
        'food_type',
        'actual_price',
        'stop',
        'z_index',
        'created_at',
        'updated_at',
    )

    list_editable = [
        'z_index',
        'actual_price',
        'stop',
    ]
    search_fields = ['name']
    list_filter = ['food_type__category__client', 'food_type__category', 'food_type']
    list_display_links = (
        'id',
        'name',
    )

    fieldsets = (
        (
            'Главная информация',
            {
                'fields': (
                    'food_type',
                    'name',
                    'actual_price',
                    'stop',
                )
            },
        ),
        (
            'Необязательная информация',
            {
                'fields': (
                    'z_index',
                    'image',
                    'description',
                    'old_price',
                    'popular',
                    'spicy',
                    'vegetarian',
                )
            },
        ),
        (
            'Административная информация',
            {
                'fields': (
                    'generated',
                    'created_at',
                    'updated_at',
                )
            },
        ),
    )

    def get_client_name(self, obj):
        return (
            obj.food_type.category.client.name
            if obj.food_type
            and obj.food_type.category
            and obj.food_type.category.client
            else "Нет клиента"
        )

    get_client_name.short_description = "Client"  # Задаем заголовок колонки
