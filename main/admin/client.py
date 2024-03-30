from django.contrib import admin

from main.models import Client

admin.site.site_header = "YAEM"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at')
    prepopulated_fields = {"url_name": ("name",)}
    list_display = (
        'id',
        'name',
        'user',
        'url_name',
        'city',
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
                    'translated',
                    'z_index',
                    'created_at',
                    'updated_at',
                )
            },
        ),
    )
