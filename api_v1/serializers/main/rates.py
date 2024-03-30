from rest_framework import serializers
from main.models import EstablishmentRates

class EstablishmentRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstablishmentRates
        fields = (
            'name',
        )