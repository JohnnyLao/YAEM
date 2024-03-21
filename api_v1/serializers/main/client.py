from rest_framework import serializers

from api_v1.serializers.main import CityRUDSerializer
from main.models import Client


class ClientBaseInfoListSerializer(serializers.ModelSerializer):
    # serializer provides basic information about a list of user establishment,
    class Meta:
        model = Client
        fields = (
            'id',
            'name',
            'description',
            'address',
        )


class ClientRUDSerializer(serializers.ModelSerializer):
    # serializer for retrieving, updating, and deleting user establishment information.

    class Meta:
        model = Client
        fields = (
            'id',
            'name',
            'description',
            'address',
        )

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     main_info = {}
    #     for field in self.Meta.read_only_fields:
    #         main_info[field] = representation.pop(field)
    #     representation['main_info'] = main_info
    #     return representation


class ClientCreateSerializer(serializers.ModelSerializer):
    # serializer for creating a new establishment.
    class Meta:
        model = Client
        fields = ('name',)
