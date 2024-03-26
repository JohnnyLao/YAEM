from rest_framework.serializers import ModelSerializer
from main.models import Category


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )
