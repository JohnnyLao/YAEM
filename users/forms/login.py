from django import forms
from phonenumber_field.formfields import PhoneNumberField


class LoginForm(forms.Form):
    phone_number = PhoneNumberField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "class": "form-control",
                "placeholder": "Введите номер телефона",
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control",
                "placeholder": "Введите пароль",
            }
        ),
    )
