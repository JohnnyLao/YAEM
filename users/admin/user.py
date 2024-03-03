from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from users.admin.profile import ProfileInlineAdmin
from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    change_user_password_template = None
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "email",
                    "username",
                )
            },
        ),
        (
            ("Личная информация"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    'is_corporate',
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "phone_number",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    list_display = (
        'id',
        'get_full_name',
        'phone_number',
        'email',
    )
    list_display_links = (
        'id',
        'get_full_name',
    )
    inlines = (ProfileInlineAdmin,)

    def get_full_name(self, obj):
        return obj.full_name

    get_full_name.short_description = 'Имя пользователя'

    # def get_readonly_fields(self, request, obj=None):
    #     read_only_fields = super().get_readonly_fields(request, obj)
    #     if not request.user.is_superuser:
    #         return read_only_fields + ('is_corporate',)
    #     return read_only_fields