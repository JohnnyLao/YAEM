from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from phonenumber_field.phonenumber import to_python


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Overriding password field, hidden data
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    phone_number = PhoneNumberField(region='KZ')

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

    # Custom validation for phone_number field
    def validate_phone_number(self, value):
        # Convert input value to phone number object
        phone_number = to_python(value)
        if not phone_number:
            raise serializers.ValidationError("Invalid phone number format.")
        # Check if the phone number already exists
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("This phone number is already registered.")
        return phone_number

    # Overriding create method, when requesting a post, create it in the user's database
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
