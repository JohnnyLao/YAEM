from datetime import datetime, timedelta
from string import ascii_letters, digits, punctuation

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from main.models import City, Client


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
        fields = (
            'user',
            'id',
            'name',
            'url_name',
            'city',
            'description',
            'logo',
            'status',
            'tarif_number',
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
            'user',
            'id',
            'name',
            'url_name',
            'city',
            'work_time_start',
            'work_time_end',
            'logo',
            'description',
            'address',
            'phone',
            'inst',
            'two_gis',
            'outside',
            'delivery',
            'service',
            'wifi',
            'wifi_password',
            'tarif_number',
            'status',
        )

    # Name validations
    def validate_name(self, value):
        # Remove spaces from the name and check if it contains only ru/en characters
        if len(str(value)) >= 30:
            raise ValidationError(
                'Max len error'
            )
        if not str(value).replace(' ', '').isalpha():
            raise ValidationError(
                'The name can only contain letters (Russian and English)'
            )
        return str(value).title()

    # URL name validations
    def validate_url_name(self, value):
        # Check if the instance exists and if the URL name is unchanged
        if self.instance and self.instance.url_name == value:
            return value
        # Check if a Client with the same URL name already exists
        if Client.objects.filter(url_name=value).exists():
            raise ValidationError('Заведение с таким /url уже существует.')
        # Remove spaces from the URL name and check if it contains only Latin characters
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

    # Name validations
    def validate_name(self, value):
        # Remove spaces from the name and check if it contains only ru/en characters
        name = str(value).replace(' ', '').isalpha()
        if not name:
            raise ValidationError(
                'The name can only contain letters (Russian and English)'
            )
        return str(value).title()

    # URL validations
    def validate_url_name(self, value):
        # Remove spaces from the URL name and check if it contains only Latin characters
        url_name = str(value).replace(' ', '')
        if any(char not in ascii_letters for char in url_name):
            raise ValidationError('The URL name can only contain Latin characters')
        return str(value).lower().replace(' ', '-')

    # Override the create method
    def create(self, validated_data):
        # Get current user
        current_user = self.context['request'].user

        # Check if the user exceeds the limit on the number of establishments (no more than three)
        if current_user.get_user_establishments.count() >= 3:
            raise ValidationError(
                "Вы превысили лимит на количество созданных заведений"
            )

        # Get the current time
        current_time = datetime.now()
        # Calculate the payment date 30 days ahead from the current time
        paid_at = current_time + timedelta(days=30)
        # Get city name from data
        city_name = validated_data.pop('city')
        # Get this city
        city = City.objects.get(name=city_name)
        # Create a Client object with set values
        client = Client.objects.create(city=city, paid_at=paid_at, **validated_data)
        return client
