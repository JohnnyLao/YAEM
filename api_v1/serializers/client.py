from rest_framework import serializers

from main.models import Client


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "z_index",
            "name",
            "status",
        )


class ClientRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "z_index",
            "name",
            "description",
            "working_time",
            "address",
            "phone",
            "inst",
            "two_gis",
        )
