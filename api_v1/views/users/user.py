from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.serializers.users import UserRegistrationSerializer


@extend_schema_view(
    post=extend_schema(summary="Create a new user", tags=["Users: Utils"]),
)
class UserRegistrationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    # all users can register in API
    permission_classes = [permissions.AllowAny]


@extend_schema_view(
    get=extend_schema(summary="Get user phone", tags=["Users: Utils"]),
)
class UserPhoneNumberView(APIView):
    # Get only user phone number
    def get(self, request):
        user_phone_number = request.user.phone_number
        if user_phone_number:
            return Response(
                {'phone_number': str(user_phone_number)}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'Номер телефона не найден'}, status=status.HTTP_404_NOT_FOUND
            )
