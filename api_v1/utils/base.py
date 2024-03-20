from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class CustomModelViewSet(ModelViewSet):
    """
    A custom view set that provides flexibility in defining multiple serializer classes
    and permission classes based on the action performed.
    """

    multi_serializer_classes = (
        None  # Dictionary to store serializer classes for different actions
    )
    multi_permission_classes = (
        None  # Dictionary to store permission classes for different actions
    )
    serializer_class = None  # Default serializer class if not specified for an action

    def get_serializer_class(self):
        """
        Returns the serializer class based on the action performed.
        """
        if not self.multi_serializer_classes:
            raise ValueError(
                "multi_serializer_classes not found"
            )  # Raise error if serializer classes not defined
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
            for permission in self.multi_permission_classes.get(
                self.action, [IsAuthenticated]
            )
        ]
