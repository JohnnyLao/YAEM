from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticated

from api_v1.serializers import main
from api_v1.utils.base import CustomModelViewSet
from api_v1.utils.permissions import IsEstablishmentOwnerOrAdmin
from main.models import Client


@extend_schema_view(
    list=extend_schema(
        summary="Return base info list of all establishments for user",
        tags=["Menu: Clients"],
    ),
    retrieve=extend_schema(
        summary="Retrieve full information about an establishment for user",
        tags=["Menu: Clients"],
    ),
    create=extend_schema(
        summary="Create a new establishment for user", tags=["Menu: Clients"]
    ),
    update=extend_schema(
        summary="Completely modify data in an establishment for user",
        tags=["Menu: Clients"],
    ),
    partial_update=extend_schema(
        summary="Partially modify data in an establishment for user",
        tags=["Menu: Clients"],
    ),
    destroy=extend_schema(
        summary="Delete an establishment for user", tags=["Menu: Clients"]
    ),
)
class ClientViewSet(CustomModelViewSet):
    queryset = Client.objects.all()
    multi_serializer_classes = {
        # get base list info
        'list': main.ClientBaseInfoListSerializer,
        # create establishment
        'create': main.ClientCreateSerializer,
        # get full info about establishment
        'retrieve': main.ClientRUDSerializer,
        # update full info about establishment
        'update': main.ClientRUDSerializer,
        # update partial info about establishment
        'partial_update': main.ClientRUDSerializer,
        # delete establishment
        'destroy': main.ClientRUDSerializer,
    }
    multi_permission_classes = {
        # admin group or current user have permission on 'list' method
        'list': [IsEstablishmentOwnerOrAdmin],
        # admin group or current user have permission on 'retrieve' method
        'retrieve': [IsEstablishmentOwnerOrAdmin],
        # any users have permission on 'create' method
        'create': [IsAuthenticated],
        # admin group or current user have permission on 'update' method
        'update': [IsEstablishmentOwnerOrAdmin],
        # admin group or current user have permission on 'partial' update method
        'partial_update': [IsEstablishmentOwnerOrAdmin],
        # admin group or current user has permission on 'destroy' method
        'destroy': [IsEstablishmentOwnerOrAdmin],
    }

    def get_queryset(self):
        user = self.request.user
        # Admin group can see all establishments
        if user.is_staff or user.is_superuser:
            return self.queryset
        # Authenticated users can only see their establishments
        if user.is_authenticated:
            # list action returns only user's establishment
            if self.action == 'list':
                return self.queryset.filter(user=user)
            else:
                return self.queryset
