from django import forms


class LoginForm(forms.Form):
    Login = forms.CharField(max_length=100)
    Password = forms.CharField(widget=forms.PasswordInput())
