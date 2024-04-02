from django.contrib import admin

from main.models import Food_type


@admin.register(Food_type)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'd_name', 'category', 'z_index')
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
            {
                'fields': (
                    'name',
                    'category',
                    'z_index',
                )
            },
        ),
        (
            'Административная информация',
            {'fields': ('d_name',)},
        ),
    )
