from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        return redirect("login")

    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect("profile")

    return render(request, "login.html")


@login_required(login_url="login")
def profile_view(request):
    return render(request, "profile.html")


def logout_view(request):
    logout(request)
    return redirect("login")