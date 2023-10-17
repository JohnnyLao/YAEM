from django.shortcuts import render
from django.views.generic import TemplateView


class Register(TemplateView):
    template_name = "accounts/register.html"


class Login(TemplateView):
    template_name = "accounts/login.html"


class Dashboard(TemplateView):
    template_name = "accounts/dashboard.html"
