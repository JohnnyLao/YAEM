from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api_v1.serializers import main
from api_v1.utils.base import CustomModelViewSet
from api_v1.utils.permissions import IsSubcategoryOwner
from main.models import Client, Food_type, Category


@extend_schema_view(
    list=extend_schema(
        summary="Return base info list of all user's subcategories, if param - category_id exists, Get all subcategories associated with this categories",
        tags=["Menu: Subcategories"],
    ),
    # retrieve=extend_schema(
    #     summary="Retrieve full information about an user's subcategory",
    #     tags=["Menu: Subcategories"],
    # ),
    create=extend_schema(
        summary="Create a new user's subcategory", tags=["Menu: Subcategories"]
    ),
    update=extend_schema(
        summary="Completely modify data in an user's subcategory",
        tags=["Menu: Subcategories"],
    ),
    partial_update=extend_schema(
        summary="Partially modify data in an subcategory for user",
        tags=["Menu: Subcategories"],
    ),
    destroy=extend_schema(
        summary="Delete an user's subcategory", tags=["Menu: Subcategories"]
    ),
)
class SubcategoryViewSet(CustomModelViewSet):
    queryset = Food_type.objects.all()
    # Serializers
    multi_serializer_classes = {
        # When acting on a 'list', a specific serializer is used
        'list': main.SubcategoryBaseInfoListSerializer,
        # When acting on a 'create', a specific serializer is used
        'create': main.SubcategoryCreateSerializer,
        # When acting on a 'retrieve', a specific serializer is used
        # 'retrieve': main.SubcategoryRUDSerializer,
        # When acting on a 'update', a specific serializer is used
        'update': main.SubcategoryRUDSerializer,
        # When acting on a 'partial update', a specific serializer is used
        'partial_update': main.SubcategoryRUDSerializer,
        # When acting on a 'destroy', a specific serializer is used
        'destroy': main.SubcategoryRUDSerializer,
    }
    # Permissions
    multi_permission_classes = {
        # Only the subcategory creator can interact with them through an action 'list'
        'list': [IsSubcategoryOwner],
        # Only the subcategory creator can interact with them through an action 'retrieve'
        # 'retrieve': [IsCategoryOwner],
        # Only the authenticated users can interact with them through an action 'create'
        'create': [IsAuthenticated],
        # Only the subcategory creator can interact with them through an action 'update'
        'update': [IsSubcategoryOwner],
        # Only the subcategory creator can interact with them through an action 'partial update'
        'partial_update': [IsSubcategoryOwner],
        # Only the category creator can interact with them through an action 'destroy'
        'destroy': [IsSubcategoryOwner],
    }

    # Override the action 'list' to get unique user subcategories and categories
    def list(self, request, *args, **kwargs):
        current_user = request.user
        if current_user.is_authenticated:
            # Get ID from request params (?category_id=*)
            category_id = request.query_params.get('category_id')
            if category_id is not None:
                category = Category.objects.get(id=int(category_id))
                # Check if the current user has access
                if category.client.user == current_user:
                    # Get all subcategories associated with this category
                    queryset = self.queryset.filter(category_id=int(category_id))
                    serializer = self.get_serializer(queryset, many=True)
                    return Response(serializer.data)
                else:
                    return Response({"detail": "You do not have permission to access this action."},
                                    status=status.HTTP_403_FORBIDDEN)
            else:
                # If not ID, get all subcategories created by the user
                if current_user.is_authenticated:
                    # Retrieving all categories created by the user
                    queryset = self.queryset.filter(category__client__user=current_user)
                    serializer = self.get_serializer(queryset, many=True)
                    return Response(serializer.data)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        return Response('Permission denied')
