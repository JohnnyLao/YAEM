from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from main.models import Category, Client, Dish, Food_type


# The sheet is called upon action 'list' and provides basic information
class DishListSerializer(serializers.ModelSerializer):
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


class DishRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            'id',
            'z_index',
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
        extra_kwargs = {
            'image': {'required': False},
        }


class DishCreateSerializer(serializers.ModelSerializer):
    # Create field for subcategory id
    food_type_id = serializers.IntegerField()

    class Meta:
        model = Dish
        fields = (
            'food_type_id',
            'z_index',
            'actual_price',
            'old_price',
            'description',
            'stop',
            'image',
            'popular',
            'spicy',
            'vegetarian',
        )
        # Optional fields
        extra_kwargs = {
            'image': {'required': False},
            'old_price': {'required': False},
            'description': {'required': False},
            'stop': {'required': False},
            'popular': {'required': False},
            'spicy': {'required': False},
            'vegetarian': {'required': False},
        }

    def create(self, validated_data):
        # Get the subcategory ID from the data
        subcategory_id = validated_data.pop('food_type_id')
        # Get the subcategory by its ID
        subcategory = Food_type.objects.get(id=int(subcategory_id))
        # Create a dish associated with this client
        dish = Dish.objects.create(food_type=subcategory, **validated_data)
        return dish
