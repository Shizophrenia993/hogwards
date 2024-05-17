from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from src.apps.users.forms import LoginForm, RegisterForm
from src.apps.users.models import User


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                return render(request, 'login.html', {'error': 'Неверное имя пользователя или пароль'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
