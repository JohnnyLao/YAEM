from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from main.models import Category, Client, Food_type


# The sheet is called upon action 'list' and provides basic information
class SubcategoryBaseInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_type
        fields = (
            'id',
            'name',
        )


class SubcategoryRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_type
        fields = (
            'id',
            'name',
        )


class SubcategoryCreateSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()

    class Meta:
        model = Food_type
        fields = (
            'category_id',
            'name',
        )

    def create(self, validated_data):
        # Get the category ID from the data
        category_id = validated_data.pop('category_id')
        # Get the category by its ID
        category = Category.objects.get(id=int(category_id))

        # Permission - only the creator of the category can create a subcategory for himself
        if not self.context['request'].user == category.client.user:
            raise PermissionDenied(
                "You do not have permission to create a subcategory for this client."
            )

        # Create a category associated with this client
        subcategory = Food_type.objects.create(category=category, **validated_data)
        return subcategory
