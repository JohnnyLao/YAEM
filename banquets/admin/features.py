from django.contrib import admin

from banquets.models import FeaturesOfTheBanquetHall


@admin.register(FeaturesOfTheBanquetHall)
class FeaturesOfTheBanquetHallAdmin(admin.ModelAdmin):
    search_fields = ("features_name",)
