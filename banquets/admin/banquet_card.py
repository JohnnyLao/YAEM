from django.contrib import admin

from banquets.models import BanquetCard


@admin.register(BanquetCard)
class BanquetCardAdmin(admin.ModelAdmin):
    list_display = (
        "z_index",
        "name",
        "status",
        "city",
    )
