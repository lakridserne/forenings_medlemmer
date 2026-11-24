from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Email adresse",
        widget=forms.TextInput(attrs={
            "placeholder": "Email adresse",
            "autocomplete": "username",
        })
    )
