from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from ckeditor.fields import RichTextField

from datetime import date

# Create your models here.
class User(AbstractUser):
    pass 


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=280, default="CS50 Web Final Project")
    date_join = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100, null=True, blank=True) 
    image_url = models.URLField(default="https://cdn.shopify.com/s/files/1/1132/3108/files/NZ_corner_400x.jpg?v=1603743748")
    def __str__(self):
        return f"{self.username}"


class Destination(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100, null=True, blank=True) 
    image_url = models.URLField(null=True, blank=True)
    wishlist = models.ManyToManyField(User, related_name='destination_wishlist', blank=True)
    def __str__(self):
        return f"{self.title} | {self.author}"


class Food(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100, null=True, blank=True) 
    image_url = models.URLField(null=True, blank=True)
    wishlist = models.ManyToManyField(User, related_name='food_wishlist', blank=True)
    def __str__(self):
        return f"{self.title} | {self.author}"


class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100, null=True, blank=True) 
    image_url = models.URLField(null=True, blank=True)
    wishlist = models.ManyToManyField(User, related_name='event_wishlist', blank=True)
    def __str__(self):
        return f"{self.title} | {self.author}"


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    short_description = models.CharField(max_length=200, default='Short description')
    # body = models.TextField(null=True, blank=True)
    image_url = models.URLField(default='https://blog.airpaz.com/wp-content/uploads/Indonesia-1.jpg')
    body = RichTextField(null=True, blank=True)
    date_created = models.DateField(default=timezone.now)
    wishlist = models.ManyToManyField(User, related_name='blog_wishlist', blank=True)
    def __str__(self):
        return f"{self.title} | {self.author}"

# Automatically create Profile model when User after register a User
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)
        print('Profile created!')


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profile updated!')
