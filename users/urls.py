from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('signin/', views.LoginView.as_view(), name='signin'),
    path('signup/', views.RegistrationView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
