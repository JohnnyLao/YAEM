from rest_framework.serializers import ModelSerializer

from main.models import City


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )


class CityDetailSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('name',)
