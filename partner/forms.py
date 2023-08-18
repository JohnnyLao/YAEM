from django import forms
from django.core.mail import send_mail
from django.utils.translation import gettext
from validate_email import validate_email


class FeedBackForm(forms.Form):
    name = forms.CharField(max_length=20, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control text-light'}))
    email = forms.EmailField(max_length=50, required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control text-light'}))
    phone = forms.CharField(max_length=20, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control text-light'}))

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <= 3:
            raise forms.ValidationError(gettext("Имя должно содержать больше 3 символов."))
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not validate_email(email):
            raise forms.ValidationError(gettext('Введите корректный адрес электронной почты.'))
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) <= 5 or phone.isalpha():
            raise forms.ValidationError(gettext('Введите корректный телефонный номер.'))
        return phone

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        subject = 'Здравствуйте, я с сайта YaEm'
        message = f'Имя: {name}\nEmail: {email}\nТелефон: {phone}'
        recipient_list = ['y4.3m@yandex.ru']
        send_mail(subject, message, email, recipient_list)
