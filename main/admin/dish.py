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
        'created_at',
        'updated_at',
    )
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
                    'z_index',
                    'created_at',
                    'updated_at',
                )
            },
        ),
    )
