from django.urls import path
from django.views.decorators.cache import cache_page
from accounts.views import Dashboard, CustomSignupView, CustomLoginView, CustomLogoutView, CustomChangePasswordView, CustomResetPasswordView
from django.conf import settings

cache_duration = 0
# accounts:change_password
# accounts:reset_password
app_name = "accounts"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", CustomSignupView.as_view(), name="signup"),
    path('logout/', CustomLogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('change/password/', CustomChangePasswordView.as_view(), name='change_password'),
    path('reset/password/', CustomResetPasswordView.as_view(), name='reset_password'),
    # path("dashboard", cache_page(cache_duration)(Dashboard.as_view()), name="dashboard"),
]
