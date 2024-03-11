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
        if not self.multi_permission_classes:
            raise ValueError("multi_permission_classes not found")
        return [
            permission()
            for permission in self.multi_permission_classes.get(
                self.action, [IsAuthenticated]
            )
        ]
