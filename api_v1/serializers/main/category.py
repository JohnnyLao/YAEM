from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from main.models import Category, Client


# The sheet is called upon action 'list' and provides basic information
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'z_index',
            'name',
            'bg_image',
            'is_active',
        )


# The sheet is called upon action 'retrieve/update/partial update/destroy' and provides detail information
class CategoryRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'z_index',
            'name',
            'bg_image',
            'is_active',
        )


# The sheet is called upon action 'create'
class CategoryCreateSerializer(serializers.ModelSerializer):
    # Add a field to get the client ID
    client_id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = (
            'client_id',
            'z_index',
            'name',
            'bg_image',
            'is_active',
        )
        # Optional fields
        extra_kwargs = {
            'z_index': {'required': False},
            'bg_image': {'required': False},
        }

    # Overriding the create method, when creating, we associate the category with the establishment
    def create(self, validated_data):
        # Get the client ID from the data
        client_id = validated_data.pop('client_id')
        # Get the client by its ID
        client = Client.objects.get(id=int(client_id))
        # Create a category associated with this client
        category = Category.objects.create(client=client, **validated_data)
        return category
