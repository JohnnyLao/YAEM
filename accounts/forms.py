# from django import forms
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'yourUsername',
#     }))
#     password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'yourPassword',
#     }))
#     remember = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
#         'class': 'form-check-input',
#         'id': 'rememberMe',
#         'checked': False
#     }))


from allauth.account.forms import LoginForm, SignupForm, ChangePasswordForm, ResetPasswordForm


class CustomLoginForm(LoginForm):
    pass


class CustomSignupForm(SignupForm):
    pass


class CustomChangePasswordForm(ChangePasswordForm):
    pass


class CustomResetPasswordForm(ResetPasswordForm):
    pass
