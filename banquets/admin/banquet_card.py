from django.contrib import admin

from banquets.models import BanquetCard


@admin.register(BanquetCard)
class BanquetCardAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "status",
        "city",
    )
    list_filter = ("city",)
