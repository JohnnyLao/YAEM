from django.contrib import admin

from main.models import EstablishmentRates


@admin.register(EstablishmentRates)
class EstablishmentRatesAdmin(admin.ModelAdmin):
    pass
