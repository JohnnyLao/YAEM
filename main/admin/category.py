from django.contrib import admin

from main.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'd_name', 'client', 'z_index')
    list_filter = ('client', 'is_active')
    list_display = (
        'id',
        'd_name',
        'client',
        'z_index',
        'is_active',
    )
    list_editable = ["z_index"]
    list_display_links = (
        'id',
        'd_name',
    )

    fieldsets = (
        (
            'Главная информация',
            {
                'fields': (
                    'z_index',
                    'client',
                    'name',
                )
            },
        ),
        (
            'Административная информация',
            {
                'fields': (
                    'is_active',
                    'bg_image',
                    'd_name',
                )
            },
        ),
        (
            'Переводы',
            {
                'fields': (
                    'name_en',
                    'name_kk',
                )
            },
        ),
    )
