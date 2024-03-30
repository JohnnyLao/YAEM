from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import main
from main.models import City


@extend_schema_view(
    list=extend_schema(summary="List of all cities", tags=["Menu: Cities"]),
)
class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = main.CitySerializer
    http_method_names = ("get",)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        pass
