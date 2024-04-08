from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from main.models import Category, Client, Food_type


# The sheet is called upon action 'list' and provides basic information
class SubcategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_type
        fields = (
            'id',
            'z_index',
            'name',
        )


class SubcategoryRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_type
        fields = (
            'id',
            'z_index',
            'name',
        )

    def validate_name(self, value):
        if not str(value).replace(' ', '').isalnum():
            raise ValidationError('Subcategory: only ru/en/num characters')
        return str(value).capitalize()


class SubcategoryCreateSerializer(serializers.ModelSerializer):
    # Create field for category id
    category_id = serializers.IntegerField()

    class Meta:
        model = Food_type
        fields = (
            'category_id',
            'name',
        )

    def validate_name(self, value):
        if not str(value).replace(' ', '').isalnum():
            raise ValidationError('Subcategory: only ru/en/num characters')
        return str(value).capitalize()

    def create(self, validated_data):
        # Get the category ID from the data
        category_id = validated_data.pop('category_id')
        # Get the category by its ID
        category = Category.objects.get(id=int(category_id))
        # Create a category associated with this client
        subcategory = Food_type.objects.create(category=category, **validated_data)
        return subcategory
