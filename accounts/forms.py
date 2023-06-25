from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'id': 'validationDefaultUsername',
                'type': 'text',
                'aria-describedby': 'inputGroupPrepend2'
            }
        ),
        required=True
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'inputPassword',
                'type': 'password'
            }
        ),
        required=True
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='username',
        required=True,
        max_length=30,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'id': 'validationDefaultUsername',
                'type': 'text',
                'aria-describedby': 'inputGroupPrepend2'
            }
        ),
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'inputPassword',
                'type': 'password'
            }
        ),
    )

    password2 = forms.CharField(
        label='Password',
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat Password',
                'id': 'inputPassword',
                'type': 'password'
            }
        ),
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
