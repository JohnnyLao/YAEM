from django.contrib import admin

from banquets.models import Banquet


@admin.register(Banquet)
class BanquetAdmin(admin.ModelAdmin):
    list_display = ("banquet_card", "name", "get_city")
    list_filter = ("banquet_card",)
    filter_horizontal = ["kitchen_types", "features_name"]

    def get_city(self, obj):
        city = obj.banquet_card.city
        if not city:
            return "Город не указан"
        return obj.banquet_card.city

    get_city.short_description = "Город"
