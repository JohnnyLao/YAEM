from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import ListAPIView, GenericAPIView
from api_v1.serializers import main
from main.models import Category


@extend_schema_view(
    list=extend_schema(
        summary="Return list of all categories",
        tags=["Menu: Categories"],
    ))
class CategoryListView(ListAPIView, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = main.CategoryListSerializer
