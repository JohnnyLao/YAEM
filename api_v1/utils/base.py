from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class CustomModelViewSet(ModelViewSet):
    multi_serializer_classes = None
    multi_permission_classes = None
    serializer_class = None

    def get_serializer_class(self):
        if not self.multi_serializer_classes:
            raise ValueError("multi_serializer_classes not found")
        return self.multi_serializer_classes.get(self.action, self.serializer_class)

    def get_permissions(self):
        """
        Returns the permission classes based on the action performed.
        """
        if not self.multi_permission_classes:
            raise ValueError(
                "multi_permission_classes not found"
            )  # Raise error if permission classes not defined
        return [
            permission()
            for permission_list in self.multi_permission_classes.values()
            for permission in permission_list
        ]
