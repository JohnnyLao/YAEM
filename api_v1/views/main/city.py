from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import main
from main.models import City


@extend_schema_view(
    list=extend_schema(summary="List of all cities", tags=["Menu: Cities"]),
)
class CityViewSet(ModelViewSet):
    # Get queryset
    queryset = City.objects.all()
    # Get list serializer
    serializer_class = main.CityListSerializer
    # Only authenticated users has permission on this method
    permission_classes = [permissions.IsAuthenticated]
    # allowing only get method
    http_method_names = ("get",)

    # turning off the retrieve method
    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        return Response('Permission denied')
