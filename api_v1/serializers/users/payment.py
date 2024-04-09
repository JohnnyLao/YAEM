from rest_framework import serializers

from users.models import Payment


# Payments list and create payment
class PaymentLCDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id',
            'tarif_number',
            'months',
            'phone',
            'created_at',
            'status',
        )
        # Optional fields
        extra_kwargs = {
            'id': {'required': False},
            'created_at': {'required': False},
        }
