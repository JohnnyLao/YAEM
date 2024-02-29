from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(login_required, name="dispatch")
class LogoutView(View):

    def get(self, request, *args, **kwargs):
        full_name = request.user.full_name
        if request.user.is_authenticated:
            logout(request)
            messages.warning(request, f"{full_name} - вы вышли из аккаунта")
            return redirect(reverse("users:signin"))
