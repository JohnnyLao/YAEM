from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api_v1.serializers import main
from api_v1.utils.base import CustomModelViewSet
from api_v1.utils.permissions import IsDishOwner
from main.models import Client, Dish, Food_type


@extend_schema_view(
    list=extend_schema(
        summary="Return base info list of all user's dishes, if param - food_type_id exists, Get all dishes associated with this categories",
        tags=["Menu: Dishes"],
    ),
    # retrieve=extend_schema(
    #     summary="Retrieve full information about an user's dishes",
    #     tags=["Menu: Dishes"],
    # ),
    create=extend_schema(summary="Create a new user's dish", tags=["Menu: Dishes"]),
    update=extend_schema(
        summary="Completely modify data in an user's dish",
        tags=["Menu: Dishes"],
    ),
    partial_update=extend_schema(
        summary="Partially modify data in an dish for user",
        tags=["Menu: Dishes"],
    ),
    destroy=extend_schema(summary="Delete an user's dish", tags=["Menu: Dishes"]),
)
class DishViewSet(CustomModelViewSet):
    queryset = Dish.objects.all()
    # Serializers
    multi_serializer_classes = {
        # When acting on a 'list', a specific serializer is used
        'list': main.DishBaseInfoListSerializer,
        # When acting on a 'create', a specific serializer is used
        'create': main.DishCreateSerializer,
        # When acting on a 'retrieve', a specific serializer is used
        # 'retrieve': main.DishRUDSerializer,
        # When acting on a 'update', a specific serializer is used
        'update': main.DishRUDSerializer,
        # When acting on a 'partial update', a specific serializer is used
        'partial_update': main.DishRUDSerializer,
        # When acting on a 'destroy', a specific serializer is used
        'destroy': main.DishRUDSerializer,
    }
    # Permissions
    multi_permission_classes = {
        # Only the dish creator can interact with them through an action 'list'
        'list': [IsDishOwner],
        # Only the dish creator can interact with them through an action 'retrieve'
        # 'retrieve': [IsDishOwner],
        # Only the authenticated users can interact with them through an action 'create'
        'create': [IsAuthenticated],
        # Only the dish creator can interact with them through an action 'update'
        'update': [IsDishOwner],
        # Only the dish creator can interact with them through an action 'partial update'
        'partial_update': [IsDishOwner],
        # Only the dish creator can interact with them through an action 'destroy'
        'destroy': [IsDishOwner],
    }

    # Override the action 'list' to get unique user dishes and subcategory
    def list(self, request, *args, **kwargs):
        current_user = request.user
        if current_user.is_authenticated:
            # Get ID from request params (?food_type_id=*)
            subcategory_id = request.query_params.get('food_type_id')
            if subcategory_id is not None:
                subcategory = Food_type.objects.get(id=int(subcategory_id))
                # Check if the current user has access
                if subcategory.category.client.user == current_user:
                    # Get all dishes associated with this subcategory
                    queryset = self.queryset.filter(food_type_id=int(subcategory_id))
                    serializer = self.get_serializer(queryset, many=True)
                    return Response(serializer.data)
                else:
                    return Response({"detail": "You do not have permission to access this action."},
                                    status=status.HTTP_403_FORBIDDEN)
            else:
                # If not ID, get all dishes created by the user
                if current_user.is_authenticated:
                    # Retrieving all dishes created by the user
                    queryset = self.queryset.filter(
                        food_type__category__client__user=current_user
                    )
                    serializer = self.get_serializer(queryset, many=True)
                    return Response(serializer.data)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        return Response('Permission denied')
