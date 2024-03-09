from rest_framework.serializers import ModelSerializer

from banquets.models import Banquet


class BanquetSerializer(ModelSerializer):
    class Meta:
        model = Banquet
        fields = ('name',)
