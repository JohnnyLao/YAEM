from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions as base_permissions
from rest_framework.authentication import TokenAuthentication

from api_v1.serializers import main
from api_v1.utils import permissions as custom_permission
from api_v1.utils.base import CustomModelViewSet
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
class ClientViewSet(CustomModelViewSet):
    queryset = Client.objects.all()
    multi_serializer_classes = {
        'list': main.ClientListSerializer,
        'retrieve': main.ClientRUDSerializer,
        'update': main.ClientRUDSerializer,
        'partial_update': main.ClientRUDSerializer,
        'create': main.ClientCreateSerializer,
    }
    multi_permission_classes = {
        'list': [base_permissions.AllowAny],
        'retrieve': [custom_permission.IsOwnerOrAdmin],
        'create': [custom_permission.IsAdminOrCorporateUser],
        'update': [custom_permission.IsOwnerOrAdmin],
        'partial_update': [custom_permission.IsOwnerOrAdmin],
        'destroy': [custom_permission.IsOwnerOrAdmin],
    }
    authentication_classes = [TokenAuthentication]
    ordering = ('id',)
    search_fields = ('name',)
    lookup_field = 'name'

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser or current_user.is_staff:
            return self.queryset
        if self.action == 'list':
            return self.queryset
        return self.queryset.filter(user=current_user)
