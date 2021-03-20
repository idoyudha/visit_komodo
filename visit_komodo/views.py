from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Profile, Destination, Event, Food, Blog

# Create your views here.
def index(request):
    destination = Destination.objects.all()[:5] # return first 5 objects
    event = Event.objects.all()[:5]
    food = Food.objects.all()[:5]
    context = {
        "destination": destination,
        "event": event,
        "food": food,
    }
    return render(request, "visit_komodo/index.html", context)

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
        return render(request, "visit_komodo/login.html")

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

def destination(request):
    destination = Destination.objects.all()[:5]
    context = {
        "destination": destination,
    }
    return render(request, "visit_komodo/destination.html", context)

def food(request):
    food = Food.objects.all()[:5]
    context = {
        "food": food,
    }
    return render(request, "visit_komodo/food.html", context)

def event(request):
    event = Event.objects.all()[:5]
    context = {
        "event": event,
    }
    return render(request, "visit_komodo/event.html", context)

@login_required(login_url='/login/')
@csrf_exempt
def add_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        category = request.POST["category"]
        photo = request.POST["photo"]
        location = request.POST["location"]
        description = request.POST["description"]
        if category == 'Destination':
            Destination.objects.create(created_by=request.user, title=title, description=description, location=location, image=photo)
        elif category == 'Food':
            Food.objects.create(created_by=request.user, title=title, description=description, location=location, image=photo)
        elif category == 'Event':
            Event.objects.create(created_by=request.user, title=title, description=description, location=location, image=photo)
        else:
            return render(request, "visit_komodo/add_listing.html", {
                "message": "Invalid category."
            })
        return HttpResponseRedirect('/')
    else:
        return render(request, "visit_komodo/add_listing.html")

@login_required(login_url='/login/')
def profile_view(request):
    user_id = request.user.id
    count_blog = Blog.objects.filter(created_by=user_id).count()
    count_destination = Destination.objects.filter(created_by=user_id).count()
    count_food = Food.objects.filter(created_by=user_id).count()
    count_event = Event.objects.filter(created_by=user_id).count()
    count_contrib = count_destination + count_food + count_event
    location = Profile.objects.values_list('location', flat=True).get(username=user_id)
    date_join = Profile.objects.values_list('date_join', flat=True).get(username=user_id)
    context = {
        "count_blog": count_blog,
        "contributions": count_contrib,
        "location": location,
        "date_join": date_join
    }
    return render(request, "visit_komodo/profile.html", context)