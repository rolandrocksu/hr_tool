from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views import generic

from .forms import LoginForm, SignUpForm


class SignInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form, 'error_message': ''})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')

        return render(
            request, 'registration/login.html',
            {
                'form': form,
                'error_message': ' Login Failed! Enter the username and password correctly',
            }
        )


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def post(self, request, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            login(request, user)

            return redirect('home')

        return render(
            request, 'registration/signup.html',
            {
                'form': form,
            }
        )


def sign_out(request):
    logout(request)
    return redirect('login')
