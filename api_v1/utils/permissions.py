from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsEstablishmentOwnerOrAdmin(permissions.BasePermission):
    message = "You do not have permissions to view other people's establishments"

    def has_object_permission(self, request, view, obj):
        # Client.user == request.user
        # Authenticated users can only see their establishments
        return bool(
            obj.user == request.user
            or request.user.is_superuser
            or request.user.is_staff
        )
