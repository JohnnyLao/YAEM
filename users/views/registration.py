from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, reverse
from django.views import View

from users.forms import RegistrationForm


class RegistrationView(View):
    template_name = 'users/signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main:main_page')
        return render(
            request=request,
            template_name=self.template_name,
            context={'form': RegistrationForm()},
        )

    def post(self, request, *args, **kwargs):
        registration_form = RegistrationForm(data=request.POST)

        if registration_form.is_valid():
            user = registration_form.save()
            login(request, user)

            message = f'{user.full_name} - вы успешно зарегистрировались!'
            messages.success(request=request, message=message)

            return redirect('main:delivery_list_page')

        return render(
            request=request,
            template_name=self.template_name,
            context={'form': registration_form},
        )
