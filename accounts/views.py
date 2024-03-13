from django.views.generic import TemplateView
from django.urls import reverse
from allauth.account.views import SignupView, LoginView, LogoutView, PasswordChangeView, PasswordResetView
from accounts.forms import CustomLoginForm, CustomSignupForm, CustomResetPasswordForm, CustomChangePasswordForm


# user login
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    # form_class = CustomLoginForm


# user register
class CustomSignupView(SignupView):
    template_name = "accounts/register.html"
    # form_class = CustomSignupForm

    def get_success_url(self):
        return reverse('accounts:login')


# user logout
class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


# user password change
class CustomChangePasswordView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    # form_class = CustomChangePasswordForm


# user password reset
class CustomResetPasswordView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    # form_class = CustomResetPasswordForm


class Dashboard(TemplateView):
    template_name = "accounts/dashboard.html"
