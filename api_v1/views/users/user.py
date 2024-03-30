from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from api_v1.serializers.users import UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer
    # all users can register in API
    permission_classes = [permissions.AllowAny]
