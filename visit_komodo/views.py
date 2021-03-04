from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User

# Create your views here.
def index(request):
    return HttpResponse("Hello, welcome to Komodo Island")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authenticate successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            context = {
                "message": "Invalid username and/or password"
            }
            return render(request, "visit_komodo/login.html", context)
    else:
        return render(request, "visit_komodo/login.htm")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches with password confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            context = {
                "message": "Both password must match"
            }
            return render(request, "visit_komodo/register.html", context)
        
        # Attempt to create new user
        try:
            user = User.objects.create_user(username)
            user.save()
        except IntegrityError:
            context = {
                "message": "Username already exist"
            }
            return render(request, "visit_komodo/register.html", context)
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "visit_komodo/register.html")

