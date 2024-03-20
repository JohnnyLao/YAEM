from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import main
from main.models import City


@extend_schema_view(
    list=extend_schema(summary="Список всех городов", tags=["Меню:Города"]),
    create=extend_schema(summary="Создать новый город", tags=["Меню:Города"]),
    destroy=extend_schema(summary="Удалить город", tags=["Меню:Города"]),
)
class CityViewSet(ModelViewSet):
    queryset = City.objects.all().order_by('id')
    serializer_class = main.CitySerializer
    http_method_names = (
        "get",
        "post",
        "delete",
    )
    ordering = ('id',)
    search_fields = ('name',)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        pass
