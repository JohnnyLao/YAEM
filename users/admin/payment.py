from django.contrib import admin

from main.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'tarif_number', 'months', 'phone', 'created_at', 'status']
    readonly_fields = ('user', 'created_at')
