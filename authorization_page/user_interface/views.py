from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, TemplateView
from .models import *
from .forms import *

class MainPageView(TemplateView):
    template_name = 'authorization/home_page.html'

class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'authorization/registration_page.html'
    success_url = reverse_lazy('login_page')

class UserLogin(LoginView):
    form_class = LoginUserForm
    template_name = 'authorization/login_page.html'
    redirect_authenticated_user = reverse_lazy('login_page')

class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'authorization/change_password.html'
    success_url = reverse_lazy('home')
    

def logout_user(request):
    logout(request)
    return redirect('home')