from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path('profile', views.profile_view, name='profile'),
    path('destination', views.destination, name='destination'),
    path('food', views.food, name='food'),
    path('event', views.event, name='event'),

    path('add_listing', views.add_listing, name='add_listing'),
]