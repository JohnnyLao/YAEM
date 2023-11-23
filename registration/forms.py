from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    # name = forms.CharField(max_length=30, required=False, help_text='Это поле обязательное, пожалуйста заполните его')

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if isinstance(name, str):
    #         raise forms.ValidationError('Имя должно содержать только буквы')
    #     return name

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
