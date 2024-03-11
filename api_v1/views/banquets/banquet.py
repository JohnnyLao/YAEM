from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import banquets
from banquets.models import Banquet


class BanquetViewSet(ModelViewSet):
    queryset = Banquet.objects.all().order_by('id')
    serializer_class = banquets.BanquetSerializer
    http_method_names = ("get", "post", "patch", 'delete')
