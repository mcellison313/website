from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })


def signup_view(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["passwordCheck"]:
            username = request.POST["username"]
            password = request.POST["password"]
            try:
                user = User.objects.create_user(username, None, password)

            except:  # username taken
                return render(request, "users/signup.html", {
                    "message": "Username Taken."
                })

            if user is not None:  # success
                login(request, user)
                return HttpResponseRedirect(reverse("index"))

        else:  # if passwords are different

            return render(request, "users/signup.html", {

                "message": "Passwords do not match."

            })

    return render(request, "users/signup.html")
