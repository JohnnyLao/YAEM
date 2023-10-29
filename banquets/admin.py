from django.contrib import admin
from banquets.models import Banquet


@admin.register(Banquet)
class BanquetAdmin(admin.ModelAdmin):
    list_display = ['name', 'z_index']
