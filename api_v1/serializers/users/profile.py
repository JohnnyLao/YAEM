from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'phone_number', 'email', 'is_corporate')
