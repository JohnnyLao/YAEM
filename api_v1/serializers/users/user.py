from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Overriding password field, hidden data
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'phone_number',
            'password',
        )

    # Default django validate password
    def validate_password(self, value):
        validate_password(value)
        return value

    # Overriding create method, when requesting a post, create it in the user's database
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
