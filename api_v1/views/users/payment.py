from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.response import Response

from api_v1.serializers import users
from users.models import Payment


@extend_schema_view(
    get=extend_schema(
        summary="Return base info list of all user's payments",
        tags=["Users: Utils"],
    ),
    post=extend_schema(summary="Create a new user's payment", tags=["Users: Utils"]),
)
class PaymentLCView(ListAPIView, CreateAPIView, GenericAPIView):
    queryset = Payment.objects.all()
    serializer_class = users.PaymentLCSerializer

    # Overriding the list method, get all payments created by the user
    def list(self, request, *args, **kwargs):
        # Get current user
        current_user = self.request.user
        try:
            if current_user.is_authenticated:
                # Get all user's payments
                queryset = self.queryset.filter(user=current_user)
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data)
        except Exception as ex:
            raise ex

    def create(self, request, *args, **kwargs):
        # Get current user
        current_user = request.user
        try:
            # Check if the user exceeds the limit on the number of payments (no more than one)
            if current_user.get_user_payments.count() >= 1:
                raise ValidationError("Payment: limit error")
            return super().create(request, *args, **kwargs)
        except Exception as ex:
            raise ex
