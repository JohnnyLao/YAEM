from django.contrib import admin

from users.models import Profile


class ProfileInlineAdmin(admin.TabularInline):
    model = Profile
    fields = ('telegram_id',)
