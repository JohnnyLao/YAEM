from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.serializers.users import UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    # all users can register in API
    permission_classes = [permissions.AllowAny]


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
