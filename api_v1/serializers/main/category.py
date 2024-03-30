from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from main.models import Category, Client


# The sheet is called upon action 'list' and provides basic information
class CategoryBaseInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


# The sheet is called upon action 'retrieve/update/partial update/destroy' and provides detail information
class CategoryRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


# The sheet is called upon action 'create'
class CategoryCreateSerializer(serializers.ModelSerializer):
    # Add a field to get the client ID
    client_id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = (
            'client_id',
            'name',
        )

    # Overriding the create method
    def create(self, validated_data):
        # Get the client ID from the data
        client_id = validated_data.pop('client_id')
        # Get the client by its ID
        client = Client.objects.get(id=client_id)

        # Permission - only the creator of the establishment can create a category for himself
        if not self.context['request'].user == client.user:
            raise PermissionDenied(
                "You do not have permission to create a category for this client."
            )

        # Create a category associated with this client
        category = Category.objects.create(client=client, **validated_data)
        return category
