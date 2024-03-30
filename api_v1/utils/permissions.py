from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


# Only the creator of the establishment can interact with it
class IsEstablishmentOwner(permissions.BasePermission):
    message = "You do not have permissions to view other people's establishments"

    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user)


# Only the creator of the category can interact with it
class IsCategoryOwner(permissions.BasePermission):
    message = "You do not have permissions to view other people's categories"

    def has_object_permission(self, request, view, obj):
        return bool(obj.client.user == request.user)
