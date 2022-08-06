from datetime import datetime

from django.shortcuts import render
import random

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm
from .models import RandomPassword


# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {})


def login_user(request):
    if request.method == 'POST':  # if someone fills out form , Post it
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:  # if user exist
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')  # routes to 'home' on successful login
        else:
            messages.success(request, 'Error logging in')
            return redirect('login')  # re routes to login page upon unsuccessful login
    else:
        return render(request, 'generator/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')


def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are now registered')
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'generator/signup.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You have edited your password')
            return redirect('home')
    else:  # passes in user information
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'generator/change_password.html', context)


# def home(request):
#     return render(request, 'generator/home.html')


def generate_password(request):
    return render(request, 'generator/generate_password.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()?><:;'))

    length = int(request.GET.get("length"))

    gen_password = ''
    for x in range(length):
        gen_password += random.choice(characters)

    return render(request, 'generator/password.html', {"password": gen_password})


def save_password(request):
    if request.method == 'POST':  # if someone fills out form , Post it
        password = request.POST['password']
        description = request.POST['description']
        created_date = datetime. now()
        pass_data = RandomPassword(password=password, description=description, created_date=created_date)
        pass_data.save()
        return render(request, 'generator/save_password.html', {"data": pass_data})
    else:
        return render(request, 'generator/home.html', {})


def saved_items(request):
    pass_data = RandomPassword.objects.order_by('-created_date').all()
    return render(request, 'generator/saved_items.html', {"data": pass_data})
