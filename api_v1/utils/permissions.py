from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Разрешение для доступа к деталям, удалению и изменению объекта только владельцем или администратором.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            obj.user == request.user
            or request.user.is_staff
            or request.user.is_superuser
        )


class IsAdminOrCorporateUser(permissions.BasePermission):
    """
    Разрешение для доступа к созданию объекта только администратором или корпоративным пользователем.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_staff
            or request.user.is_superuser
            or request.user.is_corporate
        )
