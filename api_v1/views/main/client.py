from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api_v1.serializers import main
from api_v1.utils.base import CustomModelViewSet
from api_v1.utils.permissions import IsEstablishmentOwner
from main.models import Client


@extend_schema_view(
    list=extend_schema(
        summary="Return base info list of all user's establishments",
        tags=["Menu: Clients"],
    ),
    retrieve=extend_schema(
        summary="Retrieve full information about an user's establishment",
        tags=["Menu: Clients"],
    ),
    create=extend_schema(
        summary="Create a new user's establishment", tags=["Menu: Clients"]
    ),
    update=extend_schema(
        summary="Completely modify data in an user's establishment",
        tags=["Menu: Clients"],
    ),
    partial_update=extend_schema(
        summary="Partially modify data in an user's establishment",
        tags=["Menu: Clients"],
    ),
    destroy=extend_schema(
        summary="Delete an user's establishment", tags=["Menu: Clients"]
    ),
)
class ClientViewSet(CustomModelViewSet):
    # Get queryset
    queryset = Client.objects
    # Serializers
    multi_serializer_classes = {
        # When acting on a 'list', a specific serializer is used
        'list': main.ClientListSerializer,
        # When acting on a 'create', a specific serializer is used
        'create': main.ClientCreateSerializer,
        # When acting on a 'retrieve', a specific serializer is used
        'retrieve': main.ClientRUDSerializer,
        # When acting on a 'update', a specific serializer is used
        'update': main.ClientRUDSerializer,
        # When acting on a 'partial update', a specific serializer is used
        'partial_update': main.ClientRUDSerializer,
        # When acting on a 'destroy', a specific serializer is used
        'destroy': main.ClientRUDSerializer,
    }
    # Permissions
    multi_permission_classes = {
        # Only the establishment creator can interact with them through an action 'list'
        'list': [IsEstablishmentOwner],
        # Only the establishment creator can interact with them through an action 'retrieve'
        'retrieve': [IsEstablishmentOwner],
        # Only the authenticated users can interact with them through an action 'create'
        'create': [IsAuthenticated],
        # Only the establishment creator can interact with them through an action 'update'
        'update': [IsEstablishmentOwner],
        # Only the establishment creator can interact with them through an action 'partial update'
        'partial_update': [IsEstablishmentOwner],
        # Only the establishment creator can interact with them through an action 'destroy'
        'destroy': [IsEstablishmentOwner],
    }

    # Overriding the list method, get all establishments created by the user
    def list(self, request, *args, **kwargs):
        # Get current user
        current_user = self.request.user
        # Get all user's establishments, filtered by client-user
        try:
            # Get all user's establishments, filtered by client-user
            queryset = self.queryset.filter(user=current_user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as ex:
            raise ex

    # Overriding the create method, establishment limit validation
    def create(self, request, *args, **kwargs):
        # Get current user
        current_user = request.user
        try:
            # Check if the user exceeds the limit on the number of establishments
            if current_user.get_user_establishments.count() >= 2:
                raise ValidationError("Establishment: limit error")
            return super().create(request, *args, **kwargs)
        except Exception as ex:
            raise ex
