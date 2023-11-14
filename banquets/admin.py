from django.contrib import admin
from banquets.models import Banquet, SubHall


@admin.register(Banquet)
class BanquetAdmin(admin.ModelAdmin):
    list_display = ['name', 'z_index']


# @admin.register(SubHallPhoto)
# class BanquetAdmin(admin.ModelAdmin):
#     pass


@admin.register(SubHall)
class SubHallAdmin(admin.ModelAdmin):
    list_display = ('name', 'banquet', 'kitchen_type', 'memorials', 'sub_hall_capacity', 'sub_hall_price_for_person')
    list_filter = ('banquet',)
