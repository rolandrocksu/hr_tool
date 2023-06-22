from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'id': 'inputUsername',
                'type': 'text'
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
    remember_me = forms.BooleanField(
        label='Remember me',
        required=False
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='username',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'id': 'inputUsername',
                'type': 'text'
            }
        ),
        required=True
    )
    password1 = forms.CharField(
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

    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat Password',
                'id': 'inputPassword',
                'type': 'password'
            }
        ),
        required=True
    )

    # class Meta:
    #     model = CustomUser
    #     fields = ('username', 'password1', 'password2')
