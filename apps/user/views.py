from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserSignUpForm, UserSignInForm


def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Name already exist')
            return redirect('user:sign-up')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exist')
            return redirect('user:sign-up')

        user = User.objects.create_user(
            username=username, password=password, email=email)
        user.save()
        messages.success(request, '¡User created!')
        return redirect('user:sign-in')

    return render(request, 'user/signUp.html', {'form': UserSignUpForm})


def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'¡Welcome {user}!')
            return redirect('main:home')

        messages.error(request, 'Invalid username or password')
        return redirect('user:sign-in')

    return render(request, 'user/signIn.html', {'form': UserSignInForm})


def signOut(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You are logged out')
        return redirect('/')

    messages.error(request, 'You are not logged in')
    return redirect('/')

def settings(request):
    return render(request, 'user/settings.html')

def profile(request):
    return render(request, 'user/profile.html')