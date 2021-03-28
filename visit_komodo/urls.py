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
    path('view/<str:menu>/<str:title>', views.view_detail, name='view_detail'), # will update this one for saving the template
    path('view_destination/<str:title>', views.view_destination, name='view_destination'),
    path('view_food/<str:title>', views.view_food, name='view_food'),
    path('view_event/<str:title>', views.view_event, name='view_event'),
    path('view_travelguide/<str:title>', views.view_travelguide, name='view_travelguide'),

    # create
    path('add_listing', views.add_listing, name='add_listing'),
    path('add_blog', views.add_blog, name='add_blog'),

    # API routes
    # destination
    path('destination_api', views.destination_api, name='destination_api'),
    path('destination_api_detail/<int:pk>', views.destination_api_detail, name='destination_api_detail'),
    # food
    path('food_api', views.food_api, name='food_api'),
    path('food_api_detail/<int:pk>', views.food_api_detail, name='food_api_detail'),
    # event
    path('event_api', views.event_api, name='event_api'),
    path('event_api_detail/<int:pk>', views.event_api_detail, name='event_api_detail'),
    # travel guide
    path('travelguide_api', views.travelguide_api, name='travelguide_api'),
    path('travelguide_api_detail/<int:pk>', views.travelguide_api_detail, name='travelguide_api_detail'),
]