from rest_framework.serializers import ModelSerializer

from api_v1.serializers.main import CityDetailSerializer
from main.models import Client


class ClientListSerializer(ModelSerializer):
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


class ClientDetailSerializer(ModelSerializer):
    city = CityDetailSerializer()

    class Meta:
        model = Client
        fields = (
            'name',
            'city',
            'logo',
            'description',
            'working_time',
            'address',
            'phone',
            'inst',
            'two_gis',
            'url_name',
            'service',
        )


class ClientCreateSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('name',)
