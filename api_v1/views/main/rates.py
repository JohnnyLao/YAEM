from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers.main import EstablishmentRatesSerializer
from main.models import EstablishmentRates


@extend_schema_view(
    list=extend_schema(summary="List of all rates", tags=["Menu: Rates"]),
)
class EstablishmentRatesViewSet(ModelViewSet):
    queryset = EstablishmentRates.objects.all()
    serializer_class = EstablishmentRatesSerializer
    permission_classes = [permissions.IsAdminUser]
    http_method_names = ('get',)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        return Response('Permission denied')
