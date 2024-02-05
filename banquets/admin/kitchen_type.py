from django.contrib import admin

from banquets.models import KitchenType


@admin.register(KitchenType)
class KitchenTypeAdmin(admin.ModelAdmin):
    search_fields = ("kitchen_type",)
