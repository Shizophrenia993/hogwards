from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=52)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(min_length=3, max_length=52)
