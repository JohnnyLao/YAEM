from django.contrib import admin

from main.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', "name", "slug", 'z_index',]
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ['z_index',]
