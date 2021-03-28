from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Django REST Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DestinationSerializer, FoodSerializer, EventSerializer, BlogSerializer

from .models import User, Profile, Destination, Event, Food, Blog
from .forms import BlogForm

# Create your views here.
def index(request):
    destination = Destination.objects.all()[:5] # return first 5 objects
    event = Event.objects.all()[:5]
    food = Food.objects.all()[:5]
    blog = Blog.objects.all()[:5]
    context = {
        "destination": destination,
        "event": event,
        "food": food,
        "blog": blog,
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

# Sub menu from index
def destination(request):
    destination = Destination.objects.all()[:5]
    context = {
        "destination": destination,
    }
    return render(request, "visit_komodo/submenu/destination.html", context)

def food(request):
    food = Food.objects.all()[:5]
    context = {
        "food": food,
    }
    return render(request, "visit_komodo/submenu/food.html", context)

def event(request):
    event = Event.objects.all()[:5]
    context = {
        "event": event,
    }
    return render(request, "visit_komodo/submenu/event.html", context)

def travel_guide(request):
    travel = Blog.objects.all()[:5]
    context = {
        "travel": travel,
    }
    return render(request, "visit_komodo/submenu/travel_guide.html", context)

# Go to page
def view_detail(request, submenu, title): # will update this one for saving the template
    return None

def view_destination(request, title):
    destination = Destination.objects.filter(title=title)
    all = Destination.objects.exclude(title=title)[:5]
    context = {
        "destination": destination,
        "all": all
    }
    return render(request, "visit_komodo/detail_page/destination.html", context)

def view_food(request, title):
    food = Food.objects.filter(title=title)
    all = Food.objects.exclude(title=title)[:5]
    context = {
        "food": food,
        "all": all
    }
    return render(request, "visit_komodo/detail_page/food.html", context)

def view_event(request, title):
    event = Event.objects.filter(title=title)
    all = Event.objects.exclude(title=title)[:5]
    context = {
        "event": event,
        "all": all
    }
    return render(request, "visit_komodo/detail_page/event.html", context)

def view_travelguide(request, title):
    travel = Blog.objects.filter(title=title)
    all = Blog.objects.exclude(title=title)[:5]
    context = {
        "travel": travel,
        "all": all
    }
    return render(request, "visit_komodo/detail_page/travel_guide.html", context)


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
            Destination.objects.create(author=request.user, title=title, description=description, location=location, image_url=photo)
        elif category == 'Food':
            Food.objects.create(author=request.user, title=title, description=description, location=location, image_url=photo)
        elif category == 'Event':
            Event.objects.create(author=request.user, title=title, description=description, location=location, image_url=photo)
        else:
            return render(request, "visit_komodo/add_listing.html", {
                "message": "Invalid category."
            })
        return HttpResponseRedirect('/')
    else:
        return render(request, "visit_komodo/add_listing.html")


@login_required(login_url='/login/')
@csrf_exempt
def add_blog(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.author = request.user
            data.save()
            return HttpResponseRedirect('/')
    context = {
        "form": form
    }
    return render(request, "visit_komodo/add_blog.html", context)


@login_required(login_url='/login/')
@csrf_exempt
def profile_view(request):
    user_id = request.user.id
    count_blog = Blog.objects.filter(author=user_id).count()
    count_destination = Destination.objects.filter(author=user_id).count()
    count_food = Food.objects.filter(author=user_id).count()
    count_event = Event.objects.filter(author=user_id).count()
    count_contrib = count_destination + count_food + count_event
    location = Profile.objects.values_list('location', flat=True).get(username=user_id)
    date_join = Profile.objects.values_list('date_join', flat=True).get(username=user_id)
    profile_data = Profile.objects.filter(id=user_id)
    if request.method == 'POST':
        profile_data.update(bio=request.POST["bio"], location=request.POST["location"], image_url=request.POST["image"])
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        context = {
            "count_blog": count_blog,
            "contributions": count_contrib,
            "location": location,
            "date_join": date_join,
            "profile_data": profile_data
        }
        return render(request, "visit_komodo/profile.html", context)

# API routes
# destination
@login_required(login_url='/login/')
@api_view(['GET'])
def destination_api(request):
    destination = Destination.objects.all()
    serializer = DestinationSerializer(destination, many=True)
    return Response(serializer.data)

@login_required(login_url='/login/')
@api_view(['GET', 'PUT'])
def destination_api_detail(request, pk):
    try:
        destination = Destination.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DestinationSerializer(destination, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DestinationSerializer(destination, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_request)
        
# food
@login_required(login_url='/login/')
@api_view(['GET'])
def food_api(request):
    food = Food.objects.all()
    serializer = FoodSerializer(food, many=True)
    return Response(serializer.data)

@login_required(login_url='/login/')
@api_view(['GET', 'PUT'])
def food_api_detail(request, pk):
    try:
        food = Food.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FoodSerializer(food, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_request)
        
# event
@login_required(login_url='/login/')
@api_view(['GET'])
def event_api(request):
    event = Event.objects.all()
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)

@login_required(login_url='/login/')
@api_view(['GET', 'PUT'])
def event_api_detail(request, pk):
    try:
        event = Food.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_request)
        
# travel guide
@login_required(login_url='/login/')
@api_view(['GET'])
def travelguide_api(request):
    travel = Blog.objects.all()
    serializer = BlogSerializer(travel, many=True)
    return Response(serializer.data)

@login_required(login_url='/login/')
@api_view(['GET', 'PUT'])
def travelguide_api_detail(request, pk):
    try:
        travel = Blog.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BlogSerializer(travel, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BlogSerializer(travel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_request)
        