from django.contrib import admin

from banquets.models import Banquet, FeaturesOfTheBanquetHall, KitchenType


class KitchenTypeInlineAdmin(admin.TabularInline):
    model = Banquet.kitchen_types.through
    extra = 1
    verbose_name = "Виды кухни"
    verbose_name_plural = "Виды кухни"


class FeaturesOfTheBanquetHallInlineAdmin(admin.TabularInline):
    model = Banquet.features_name.through
    extra = 1
    verbose_name = "Особенности"
    verbose_name_plural = "Особенности"


@admin.register(Banquet)
class BanquetAdmin(admin.ModelAdmin):
    list_display = ("id", "banquet_card", "name", "get_city")
    list_filter = ("banquet_card",)
    list_display_links = ('id', 'name', )
    exclude = (
        "kitchen_types",
        "features_name",
    )
    inlines = (KitchenTypeInlineAdmin, FeaturesOfTheBanquetHallInlineAdmin)

    def get_city(self, obj):
        city = obj.banquet_card.city
        if not city:
            return "Город не указан"
        return obj.banquet_card.city

    get_city.short_description = "Город"