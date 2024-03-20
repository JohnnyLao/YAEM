from rest_framework import serializers

from api_v1.serializers.main import CityRUDSerializer
from main.models import Client


class ClientListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing clients.

    This serializer provides basic information about a client,
    """

    class Meta:
        model = Client
        fields = (
            'id',
            'name',
            'description',
            'address',
            'logo',
            'status',
        )


class ClientRUDSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving, updating, and deleting client information.

    This serializer provides detailed information about a client,
    """

    city_name = serializers.CharField(source='city.name')
    tarif_number_name = serializers.CharField(source='tarif_number.name')

    class Meta:
        model = Client
        fields = (
            'name',
            'city_name',
            'logo',
            'description',
            'working_time',
            'address',
            'phone',
            'inst',
            'two_gis',
            'z_index',
            'status',
            'outside',
            'delivery',
            'translated',
            'tarif_number_name',
            'url_name',
            'service',
        )
        read_only_fields = (
            'status',
            'outside',
            'delivery',
            'translated',
            'tarif_number_name',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        main_info = {}
        for field in self.Meta.read_only_fields:
            main_info[field] = representation.pop(field)
        representation['main_info'] = main_info
        return representation


class ClientCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new client.
    """

    class Meta:
        model = Client
        fields = ('name',)
