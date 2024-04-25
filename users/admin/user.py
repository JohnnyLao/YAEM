from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    change_user_password_template = None
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "phone_number",
                    'number_of_establishments',
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
        'phone_number',
        'first_name',
        'created_at',
        'establishments_count',
        'payments_count',
    )
    list_display_links = (
        'id',
        'phone_number',
        'first_name',

    )

    # get name if user is superuser, else return phone number
    # def admin_name_or_phone_number(self, obj):
    #     if obj.first_name:
    #         return obj.first_name
    #     return obj.phone_number

    # admin_name_or_phone_number.short_description = 'Информация'

    # get user's establishments number
    def establishments_count(self, obj):
        if obj.get_user_establishments:
            establishments_count = obj.get_user_establishments.count()
            if establishments_count > 0:
                return establishments_count
        return 'Нет созданных заведений'

    establishments_count.short_description = 'Количество созданных заведений'

    # get user's payments number
    def payments_count(self, obj):
        if obj.get_user_payments:
            payments_count = obj.get_user_payments.count()
            if payments_count > 0:
                return payments_count
            return 'Нет входящих заявок'

    payments_count.short_description = 'Количество заявок на оплату'
