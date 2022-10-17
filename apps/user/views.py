from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import UserSignUpForm, UserSignInForm

def signUp(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Name already exist")
            return redirect("user:sign-up")
        elif User.objects.filter(email=email).exists():
            messages.warning(request, "Email already exist")
            return redirect("user:sign-up")
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, "¡User created!")
            return redirect("user:sign-in")

    else:
        form = UserSignUpForm()

    return render(request, "user/signUp.html", {"form": form})

def signIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "¡You are logged in!")
            return redirect("main:home")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("user:sign-in")
    else:
        return render(request, "user/signIn.html", {"form": UserSignInForm})

def signOut(request):
    auth.logout(request)
    messages.success(request, 'You are logged out')
    return redirect("/")