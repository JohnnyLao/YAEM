from django.contrib import admin

from main.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', "name", "slug"]
    prepopulated_fields = {"slug": ("name",)}
