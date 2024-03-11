from django.contrib import admin

from users.models import Profile


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile
    fields = ('telegram_id', 'user_address')
