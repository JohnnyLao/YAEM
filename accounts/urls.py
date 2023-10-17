from django.urls import path
from django.views.decorators.cache import cache_page
from accounts.views import Register, Login, Dashboard

cache_duration = 60 * 60 * 5
app_name = "accounts"

urlpatterns = [
    path(
        "login",
        cache_page(cache_duration)(Login.as_view()),
        name="login",
    ),
    path(
        "register",
        cache_page(cache_duration)(Register.as_view()),
        name="register",
    ),
    path(
        "dashboard",
        cache_page(cache_duration)(Dashboard.as_view()),
        name="dashboard",
    ),
]
