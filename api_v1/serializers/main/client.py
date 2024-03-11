from rest_framework import serializers

from api_v1.serializers.main import CityDetailSerializer
from main.models import Client


class ClientListSerializer(serializers.ModelSerializer):
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
    city_name = serializers.CharField(source='city.name')
    # user_name = serializers.CharField(source='user.first_name')
    tarif_number_name = serializers.CharField(source='tarif_number.name')

    class Meta:
        model = Client
        fields = (
            # 'user_name',
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
            # 'user_name',
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
    class Meta:
        model = Client
        fields = ('name',)
