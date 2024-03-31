from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from main.models import Category, Client, Dish, Food_type


# The sheet is called upon action 'list' and provides basic information
class DishBaseInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            'id',
            'name',
            'description',
            'actual_price',
            'stop',
            'image',
        )


class DishRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            'id',
            'name',
            'description',
            'actual_price',
            'old_price',
            'stop',
            'image',
            'popular',
            'spicy',
            'vegetarian',
        )


class DishCreateSerializer(serializers.ModelSerializer):
    food_type_id = serializers.IntegerField()

    class Meta:
        model = Dish
        fields = (
            'food_type_id',
            'name',
            'actual_price',
            'image',
        )
        # Optional fields
        extra_kwargs = {'image': {'required': False}}

    def create(self, validated_data):
        # Get the subcategory ID from the data
        subcategory_id = validated_data.pop('food_type_id')
        # Get the subcategory by its ID
        subcategory = Food_type.objects.get(id=int(subcategory_id))

        # Permission - only the creator of the subcategory can create a dish for himself
        if not self.context['request'].user == subcategory.category.client.user:
            raise PermissionDenied(
                "You do not have permission to create a dish for this client."
            )

        # Create a dish associated with this client
        dish = Dish.objects.create(food_type=subcategory, **validated_data)
        return dish
