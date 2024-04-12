import re
from string import ascii_letters, digits, punctuation

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from main.models import City, Client


# The sheet is called upon action 'list' and provides basic information
class ClientListSerializer(serializers.ModelSerializer):
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
            'paid_at',
        )


# The sheet is called upon action 'retrieve/update/partial update/destroy' and provides detail information
class ClientRUDSerializer(serializers.ModelSerializer):
    # Serializer for the "user" field for correct display and only read
    user = serializers.CharField(max_length=100, read_only=True)
    # Serializer for the "name" field for correct display and not required
    name = serializers.CharField(max_length=100, required=False)
    # Serializer for the "url_name" field for correct display and not required
    url_name = serializers.CharField(max_length=100, required=False)
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
        extra_kwargs = {
            'logo': {'required': False},
        }

    # Name validations
    def validate_name(self, value):
        if value:
            # Remove spaces from the name and check if it contains only ru/en/digits characters
            name = str(value).replace(' ', '').isalnum()
            if not name:
                raise ValidationError('Name: only ru/en/num characters')
            return str(value).capitalize()

    # URL name validations
    def validate_url_name(self, value):
        if value:
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

    # Phone validations
    def validate_phone(self, value):
        if value:
            # Checking that the phone number matches the pattern
            pattern = r'^(7|8)\d{10}$'
            if not re.match(pattern, str(value)):
                raise ValidationError(
                    'Phone: correct format - "+7XXXXXXXXXX" or "8XXXXXXXXXX"'
                )
            return value

    # Instagram link validations
    def validate_inst(self, value):
        if value:
            # Checking that the link matches the pattern
            if 'https://www.instagram.com/' not in str(value):
                raise ValidationError(
                    'Instagram error: pattern - https://www.instagram.com/*'
                )
            return value

    # Two gis link validations
    def validate_two_gis(self, value):
        if value:
            # Checking that the link matches the pattern
            if '2gis' not in str(value):
                raise ValidationError('Two gis error: pattern - https://2gis/*/*')
            return value

    # Service percent validations
    def validate_service(self, value):
        if value:
            # Checking that the service in range 1-100
            if not 1 <= int(value) <= 100:
                raise ValidationError('Service: only range(1, 100)')
            return value
        else:
            return value


# The sheet is called upon action 'create'
class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            # Required fields
            'name',
            'url_name',
            'city',
            # Optional fields
            # 'description',
            # 'logo',
            # 'address',
            # 'phone',
            # 'inst',
            # 'two_gis',
            # 'outside',
            # 'delivery',
            # 'service',
            # 'wifi',
            # 'wifi_password',
            # 'work_time_start',
            # 'work_time_end',
        )
        # Optional fields
        # extra_kwargs = {
        #     'description': {'required': False},
        #     'logo': {'required': False},
        #     'address': {'required': False},
        #     'phone': {'required': False},
        #     'inst': {'required': False},
        #     'two_gis': {'required': False},
        #     'outside': {'required': False},
        #     'delivery': {'required': False},
        #     'service': {'required': False},
        #     'wifi': {'required': False},
        #     'wifi_password': {'required': False},
        #     'work_time_start': {'required': False},
        #     'work_time_end': {'required': False},
        # }

    # Name validations
    def validate_name(self, value):
        # Remove spaces from the name and check if it contains only ru/en/digits characters
        name = str(value).replace(' ', '').isalnum()
        if not name:
            raise ValidationError('Name: only ru/en/num characters')
        return str(value).capitalize()

    # URL validations
    def validate_url_name(self, value):
        # Remove spaces from the URL name and check if it contains only Latin characters
        url_name = str(value).replace(' ', '')
        if any(char not in ascii_letters for char in url_name):
            raise ValidationError('The URL name can only contain Latin characters')
        return str(value).lower().replace(' ', '-')

    # Phone validations
    def validate_phone(self, value):
        # Checking that the phone number matches the pattern
        pattern = r'^(7|8)\d{10}$'
        if not re.match(pattern, str(value)):
            raise ValidationError(
                'Phone: correct format - "+7XXXXXXXXXX" or "8XXXXXXXXXX"'
            )
        return value

    # Instagram link validations
    def validate_inst(self, value):
        # Checking that the link matches the pattern
        if 'instagram' not in str(value):
            raise ValidationError(
                'Instagram error: pattern - https://www.instagram.com/*'
            )
        return value

    # Two gis link validations
    def validate_two_gis(self, value):
        # Checking that the link matches the pattern
        if 'gis' not in str(value):
            raise ValidationError('Two gis error: pattern - https://2gis/*/*')
        return value

    # Service percent validations
    def validate_service(self, value):
        # Checking that the service in range 1-100
        if not 1 <= int(value) <= 100:
            raise ValidationError('Service: only range(1, 100)')
        return value

    # Override the create method
    def create(self, validated_data):
        print(validated_data)
        # Get city name from data
        city_name = validated_data.pop('city')
        print(city_name)
        # Get this city
        # city = City.objects.get(name=city_name)
        # print(city)
        # Create a Client object with set values
        client = Client.objects.create(city=city_name, **validated_data)
        return client
