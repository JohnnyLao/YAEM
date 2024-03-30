from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework import permissions

from api_v1.serializers.main import EstablishmentRatesSerializer
from main.models import EstablishmentRates

@extend_schema_view(
    get=extend_schema(
        summary="Get all rates",
        tags=["Menu: Rates"],
    ))
class EstablishmentRatesView(generics.ListAPIView):
    queryset = EstablishmentRates.objects.all()
    serializer_class = EstablishmentRatesSerializer
    permission_classes = [permissions.IsAdminUser]
