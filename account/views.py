from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from .models import CustomUser as User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required


def RegistrationUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            messages.success(request, "Регистрация прошла успешно1!")
            return HttpResponseRedirect('/auth/login')
        else:
            return messages.error(request, "Регистрация не прошла успешно2")
    else:
        form = UserRegistrationForm()
        return render(request, "registration.html", {"form": form})


def LoginUser(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data["username_or_email"]
            password = form.cleaned_data["password"]
            user = authenticate(
                request, username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Неверные данные входа")
        else:
            messages.error(request, "Форма некорректна")
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def LogoutUser(request):
    logout(request)
    return redirect('/')
