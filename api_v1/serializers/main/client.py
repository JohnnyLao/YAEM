from string import ascii_letters, digits, punctuation

from django.core.exceptions import ValidationError
from rest_framework import serializers

from main.models import Client


# The sheet is called upon action 'list' and provides basic information
class ClientBaseInfoListSerializer(serializers.ModelSerializer):
    # Serializer for the "user" field for correct display
    user = serializers.CharField(max_length=100)
    # Serializer for the "city" field for correct display
    city = serializers.CharField(max_length=50)
    # Serializer for the "tarif_number" field for correct display
    tarif_number = serializers.CharField(max_length=20)

    class Meta:
        model = Client
        # Specifies the model that this serializer works with
        fields = (
            'user',  # User fields
            'id',  # ID field
            'name',  # Name field
            'url_name',  # URL name field
            'city',  # City fields
            'description',  # Description field
            'logo',  # Logo field
            'status',  # Status field
            'tarif_number',  # Tariff number field
        )


# The sheet is called upon action 'retrieve/update/partial update/destroy' and provides detail information
class ClientRUDSerializer(serializers.ModelSerializer):
    # Serializer for the "user" field for correct display and only read
    user = serializers.CharField(max_length=100, read_only=True)
    # Serializer for the "name" field for correct display and not required
    name = serializers.CharField(max_length=100, required=False)
    # Serializer for the "url_name" field for correct display and not required
    url_name = serializers.CharField(max_length=100, required=False)
    # Serializer for the "city" field for correct display and not required
    city = serializers.CharField(max_length=50, required=False)
    # Serializer for the "tarif_number" for correct display and only read
    tarif_number = serializers.CharField(max_length=20, read_only=True)
    # Serializer for the "status" only read
    status = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = Client
        fields = (
            'user',  # User field (read-only)
            'id',  # Identifier
            'name',  # Establishment name
            'url_name',  # Establishment URL name
            'city',  # City where the establishment is located
            'work_time_start',  # Opening time
            'work_time_end',  # Closing time
            'logo',  # Establishment logo
            'description',  # Establishment description
            'address',  # Address
            'phone',  # Phone number
            'inst',  # Instagram handle
            'two_gis',  # Link to 2GIS
            'outside',  # Outdoor seating availability
            'delivery',  # Delivery service availability
            'service',  # Additional services
            'wifi',  # Wi-Fi availability
            'wifi_password',  # Wi-Fi password
            'tarif_number',  # Establishment tariff number (read-only)
            'status',  # Establishment status (read-only)
        )

    # Checking that the establishment name contains only russian and english letters
    def validate_name(self, value):
        if not str(value).replace(' ', '').isalpha():
            raise ValidationError(
                'The name can only contain letters (Russian and English)'
            )
        return str(value).title()

    # Checking that the URL of the establishment name contains only english letters
    def validate_url_name(self, value):
        url_name = str(value).replace(' ', '')
        if any(char not in ascii_letters for char in url_name):
            raise ValidationError('The URL name can only contain Latin characters')
        return str(value).lower().replace(' ', '-')


# The sheet is called upon action 'create'
class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'name',
            'url_name',
            'description',
            'city',
            'logo',
        )
        # Optional fields
        extra_kwargs = {'description': {'required': False}, 'logo': {'required': False}}

    # Checking that the establishment name contains only russian and english letters
    def validate_name(self, value):
        name = str(value).replace(' ', '').isalpha()
        if not name:
            raise ValidationError(
                'The name can only contain letters (Russian and English)'
            )
        return str(value).title()

    # Checking that the URL of the establishment name contains only english letters
    def validate_url_name(self, value):
        url_name = str(value).replace(' ', '')
        if any(char not in ascii_letters for char in url_name):
            raise ValidationError('The URL name can only contain Latin characters')
        return str(value).lower().replace(' ', '-')
