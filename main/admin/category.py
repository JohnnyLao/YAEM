from django.contrib import admin

from main.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name"]
    list_filter = ["name"]
