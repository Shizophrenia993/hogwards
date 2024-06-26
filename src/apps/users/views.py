from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

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
                return redirect("home")
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


@login_required(login_url=reverse_lazy("login"))
def profile_view(request):
    user = request.user
    reservations = user.book_reservations.all()
    context = {'user': user, 'reservations': reservations}
    return render(request, 'profile.html', context=context)