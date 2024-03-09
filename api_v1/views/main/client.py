from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import main
from main.models import Client


@extend_schema_view(
    list=extend_schema(summary="Список всех заведений", tags=["Меню:Заведения"]),
    retrieve=extend_schema(
        summary="Полная информация о заведении", tags=["Меню:Заведения"]
    ),
    # create=extend_schema(summary="Создать новое заведение", tags=["Меню:Заведения"]),
    # update=extend_schema(
    #     summary="Полностью изменить данные в заведении", tags=["Меню:Заведения"]
    # ),
    # partial_update=extend_schema(
    #     summary="Частично изменить данные в заведении", tags=["Меню:Заведения"]
    # ),
    destroy=extend_schema(summary="Удалить заведение", tags=["Меню:Заведения"]),
)
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = main.ClientListSerializer
    # lookup_field = 'name'

    def get_serializer_class(self):
        serializer_classes = {
            'retrieve': main.ClientDetailSerializer,
            'update': main.ClientDetailSerializer,
            'partial_update': main.ClientDetailSerializer,
            'create': main.ClientCreateSerializer,
        }
        return serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        return self.queryset.order_by('id')
