from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Иван",
                "required": "true",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Иванов",
                "required": "true",
            }
        )
    )
    phone_number = PhoneNumberField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "+77777777777",
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите имя пользователя (опционально)",
            }
        ),
        required=False,
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "*youremail@example.com",
            }
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш пароль",
                "required": "true",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Подтвердите ваш пароль",
                "required": "true",
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password1",
            "password2",
        )
