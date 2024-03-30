from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api_v1.serializers import main
from api_v1.utils.base import CustomModelViewSet
from api_v1.utils.permissions import IsCategoryOwner
from main.models import Category, Client


@extend_schema_view(
    list=extend_schema(
        summary="Return base info list of all user's categories",
        tags=["Menu: Categories"],
    ),
    retrieve=extend_schema(
        summary="Retrieve full information about an user's category",
        tags=["Menu: Categories"],
    ),
    create=extend_schema(
        summary="Create a new user's category", tags=["Menu: Categories"]
    ),
    update=extend_schema(
        summary="Completely modify data in an user's category",
        tags=["Menu: Categories"],
    ),
    partial_update=extend_schema(
        summary="Partially modify data in an category for user",
        tags=["Menu: Categories"],
    ),
    destroy=extend_schema(
        summary="Delete an user's category", tags=["Menu: Categories"]
    ),
)
class CategoryViewSet(CustomModelViewSet):
    # Get queryset
    queryset = Category.objects.all()
    # Serializers
    multi_serializer_classes = {
        # When acting on a 'list', a specific serializer is used
        'list': main.CategoryBaseInfoListSerializer,
        # When acting on a 'create', a specific serializer is used
        'create': main.CategoryCreateSerializer,
        # When acting on a 'retrieve', a specific serializer is used
        'retrieve': main.CategoryRUDSerializer,
        # When acting on a 'update', a specific serializer is used
        'update': main.CategoryRUDSerializer,
        # When acting on a 'partial update', a specific serializer is used
        'partial_update': main.CategoryRUDSerializer,
        # When acting on a 'destroy', a specific serializer is used
        'destroy': main.CategoryRUDSerializer,
    }
    # Permissions
    multi_permission_classes = {
        # Only the category creator can interact with them through an action 'list'
        'list': [IsCategoryOwner],
        # Only the category creator can interact with them through an action 'retrieve'
        'retrieve': [IsCategoryOwner],
        # Only the authenticated users can interact with them through an action 'create'
        'create': [IsAuthenticated],
        # Only the category creator can interact with them through an action 'update'
        'update': [IsCategoryOwner],
        # Only the category creator can interact with them through an action 'partial update'
        'partial_update': [IsCategoryOwner],
        # Only the category creator can interact with them through an action 'destroy'
        'destroy': [IsCategoryOwner],
    }

    # Overriding the list method, get all categories created by the user
    def list(self, request, *args, **kwargs):
        # Get current user
        current_user = request.user
        if current_user.is_authenticated:
            # Get all user's categories, filtered by category-client-user
            queryset = self.queryset.filter(client__user=current_user)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
