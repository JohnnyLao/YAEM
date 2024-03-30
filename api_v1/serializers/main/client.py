from rest_framework import serializers

from main.models import Client


# The sheet is called upon action 'list' and provides basic information
class ClientBaseInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'name',
            'url_name',
        )


# The sheet is called upon action 'retrieve/update/partial update/destroy' and provides detail information
class ClientRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'name',
        )

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     main_info = {}
    #     for field in self.Meta.read_only_fields:
    #         main_info[field] = representation.pop(field)
    #     representation['main_info'] = main_info
    #     return representation


# The sheet is called upon action 'create'
class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'name',
            'city',
            'url_name',
        )
