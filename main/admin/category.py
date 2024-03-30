from django.contrib import admin

from main.models import Category

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = [
#         "name",
#     ]
#     search_fields = ["name"]
#     list_filter = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'd_name', 'client')
    list_filter = ('client', 'is_active')
    list_display = (
        'id',
        'client',
        'name',
        'd_name',
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
                    'z_index',
                )
            },
        ),
    )
