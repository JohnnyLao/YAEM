from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions as base_permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied

from api_v1.serializers import main
from api_v1.utils import permissions as custom_permission
from api_v1.utils.base import CustomModelViewSet
from main.models import Client


@extend_schema_view(
    list=extend_schema(summary="List all establishments for user", tags=["Menu: Clients"]),
    retrieve=extend_schema(
        summary="Retrieve full information about an establishment",
        tags=["Menu: Clients"],
    ),
    create=extend_schema(summary="Create a new establishment", tags=["Menu: Clients"]),
    update=extend_schema(
        summary="Completely modify data in an establishment", tags=["Menu: Clients"]
    ),
    partial_update=extend_schema(
        summary="Partially modify data in an establishment", tags=["Menu: Clients"]
    ),
    destroy=extend_schema(summary="Delete an establishment", tags=["Menu: Clients"]),
)
class ClientViewSet(CustomModelViewSet):
    """
    Custom viewset for managing establishments.

    Supports operations such as listing all establishments, retrieving, creating, updating,
    partially updating, and deleting establishments.
    """

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
    ordering = ('id',)
    search_fields = ('name',)
    lookup_field = 'name'

    def get_queryset(self):
        """
        Retrieve the queryset based on the current user's permissions.

        For listing all establishments, any user has permission.
        For retrieve, update, partial update, and destroy operations, only authenticated users have permission.
        """
        current_user = self.request.user

        # Anonymous users have no permission for retrieve, update, and delete operations
        if current_user.is_anonymous:
            raise PermissionDenied('PermissionDenied')

        # Admin group have all permissions for all operations
        # if current_user.is_superuser or current_user.is_staff:
        #     return self.queryset

        # Authenticated users have permissions for specific actions with establishments associated with them
        return self.queryset.filter(user=current_user)
