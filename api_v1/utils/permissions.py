from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permission class to allow access to object details, deletion, and modification only to the owner or administrators.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission for the requested action on the object.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            obj.user == request.user
            or request.user.is_staff
            or request.user.is_superuser
        )


class IsAdminOrCorporateUser(permissions.BasePermission):
    """
    Permission class to allow access to create an object only to administrators or corporate users.
    """

    def has_permission(self, request, view):
        """
        Check if the user has permission for the requested action.
        """
        return (
            request.user.is_staff
            or request.user.is_superuser
            # or request.user.is_corporate
        )
