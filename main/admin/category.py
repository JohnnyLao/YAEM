from django.contrib import admin

from main.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "z_index"]
    search_fields = ["name"]
    list_filter = ["name"]
