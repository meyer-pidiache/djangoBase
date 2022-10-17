from cProfile import label
from django import forms
from django.contrib.auth.models import User


class UserSignUpForm(forms.ModelForm):
    username = forms.CharField(
        max_length=20, required=True, label="Username",
        widget=forms.TextInput(attrs={
            "placeholder": "username",
            "class": "form-control",
            "id": "floatingUsername"},
        )
    )

    email = forms.CharField(
        max_length=50, required=True, label="Email address",
        widget=forms.EmailInput(attrs={
            "placeholder": "name@example.com",
            "class": "form-control",
            "id": "floatingEmail"},
        )
    )

    password = forms.CharField(
        max_length=50, required=True, label="Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control",
            "id": "floatingPassword"},
        )
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserSignInForm(forms.ModelForm):
    username = forms.CharField(
        max_length=20, required=True, label="Username",
        widget=forms.TextInput(attrs={
            "placeholder": "username",
            "class": "form-control",
            "id": "floatingUsername"},
        )
    )

    password = forms.CharField(
        max_length=50, required=True, label="Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control",
            "id": "floatingPassword"},
        )
    )

    class Meta:
        model = User
        fields = ("username", "password")
