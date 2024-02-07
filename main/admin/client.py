from django.contrib import admin

from main.models import Client

admin.site.site_header = "YAEM"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "status", "outside", "delivery"]
    list_filter = ["city", "status"]
    search_fields = ["name"]
