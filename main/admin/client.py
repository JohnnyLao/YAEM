from django.contrib import admin

from main.models import Client

admin.site.site_header = "YAEM"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', "name", "city", "status", "outside", "delivery", 'created_at', 'updated_at']
    list_filter = ["city", "status"]
    search_fields = ["name"]
