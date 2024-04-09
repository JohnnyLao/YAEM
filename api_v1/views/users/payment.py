from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.exceptions import PermissionDenied, ValidationError, NotFound
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api_v1.serializers import users
from users.models import Payment


@extend_schema_view(
    list=extend_schema(
        summary="Return base info list of all user's payments",
        tags=["Users: Utils"],
    ),
    create=extend_schema(summary="Create a new user's payment", tags=["Users: Utils"]),
    destroy=extend_schema(summary='Delete user payment', tags=['Users: Utils'])
)
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = users.PaymentLCDSerializer

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

    def destroy(self, request, *args, **kwargs):
        current_user = request.user
        try:
            instance_id = self.kwargs.get('pk')
            instance = self.queryset.get(id=instance_id)
        except Payment.DoesNotExist:
            raise NotFound('Payment not found')
        if instance.user != current_user:
            raise PermissionDenied("You don't have permission to delete this payment.")
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        return Response('Permission denied')

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        return Response('Permission denied')

    @extend_schema(exclude=True)
    def partial_update(self, request, *args, **kwargs):
        return Response('Permission denied')
