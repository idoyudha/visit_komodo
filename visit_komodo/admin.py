from django.contrib import admin
from .models import User, Profile, Destination, Food, Event

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Destination)
admin.site.register(Food)
admin.site.register(Event)