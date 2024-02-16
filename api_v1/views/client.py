from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from api_v1.serializers import ClientListSerializer, ClientRetrieveSerializer
from main.models import Client


@extend_schema_view(
    list=extend_schema(summary="Список клиентов", tags=["Клиенты"]),
    retrieve=extend_schema(summary="Детальная информация о клиенте", tags=["Клиенты"]),
)
class ClientViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    permission_classes = (IsAdminUser,)
    serializer_action_classes = {
        "retrieve": ClientRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action, self.serializer_class)
