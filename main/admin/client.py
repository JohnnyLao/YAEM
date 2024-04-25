from django.contrib import admin

from main.models import Client

admin.site.site_header = "YAEM"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)
    prepopulated_fields = {"url_name": ("name",)}
    list_filter = ['user', 'city']
    list_display = (
        'id',
        # 'user',
        'name',
        'status',
        'outside',
        'delivery',
        'paid_at',
        'created_at',
        'updated_at',
    )
    list_display_links = (
        'id',
        'name',
    )
    list_editable = ['status', 'outside', 'delivery', 'paid_at']

    fieldsets = (
        (
            'Главная информация',
            {
                'fields': (
                    'user',
                    'name',
                    'url_name',
                    'city',
                )
            },
        ),
        (
            'Необязательная информация',
            {
                'fields': (
                    'logo',
                    'description',
                    'address',
                    'phone',
                    'inst',
                    'two_gis',
                    'outside',
                    'delivery',
                    'service',
                    'wifi',
                    'wifi_password',
                    'working_time',
                    'work_time_start',
                    'work_time_end',
                )
            },
        ),
        (
            'Административная информация',
            {
                'fields': (
                    'tarif_number',
                    'status',
                    'paid_at',
                    'z_index',
                    'created_at',
                    'updated_at',
                )
            },
        ),
        (
            'Переводы',
            {
                'fields': (
                    'translated',
                    'description_en',
                    'description_kk',
                    'address_en',
                    'address_kk',
                )
            },
        ),
    )
