from django.contrib import admin

from banquets.models import (Banquet, BanquetCard, FeaturesOfTheBanquetHall,
                             KitchenType)


@admin.register(BanquetCard)
class BanquetCardAdmin(admin.ModelAdmin):
    pass


@admin.register(Banquet)
class BanquetAdmin(admin.ModelAdmin):
    filter_horizontal = ["kitchen_types", "features_name"]
    list_display = ["banquet_card", "name"]
    list_filter = ["banquet_card"]


@admin.register(KitchenType)
class KitchenTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(FeaturesOfTheBanquetHall)
class FeaturesOfTheBanquetHallAdmin(admin.ModelAdmin):
    pass
