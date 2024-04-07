from rest_framework import serializers


from users.models import Payment


class PaymentLCSerializer(serializers.ModelSerializer):
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
        extra_kwargs = {
            'id': {'required': False},
            'created_at': {'required': False},
        }

