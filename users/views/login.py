from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, reverse
from django.views import View

from users.forms import LoginForm


class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:main_page')
        return render(
            request=request,
            template_name=self.template_name,
            context={'form': LoginForm()},
        )

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(data=request.POST)

        if login_form.is_valid():
            phone_number = login_form.cleaned_data.get('phone_number')
            password = login_form.cleaned_data.get('password')
            user = authenticate(
                request=request, phone_number=phone_number, password=password
            )

            if user is not None:
                login(request, user)
                if user.first_name:
                    message = f'Добро пожаловать - {str(user.first_name).capitalize()}!'
                else:
                    message = 'Добро пожаловать!'
                messages.success(request=request, message=message)
            return redirect('main:main_page')

        return render(
            request=request,
            template_name=self.template_name,
            context={'form': login_form},
        )
