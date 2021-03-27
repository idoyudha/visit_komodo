from django.urls import path
from . import views 

urlpatterns = [
    # main url
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # sub menu
    path('profile', views.profile_view, name='profile'),
    path('destination', views.destination, name='destination'),
    path('food', views.food, name='food'),
    path('event', views.event, name='event'),
    path('travel_guide', views.travel_guide, name='travel_guide'),

    # goto page
    path('view_destination/<str:title>', views.view_destination, name='view_destination'),
    path('view_food/<str:title>', views.view_food, name='view_food'),
    path('view_event/<str:title>', views.view_event, name='view_event'),

    path('add_listing', views.add_listing, name='add_listing'),
    path('add_blog', views.add_blog, name='add_blog'),
]