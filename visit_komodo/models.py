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
    bio = models.CharField(max_length=280, default="CS50 Web Project 4 Network")
    date_join = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100, null=True, blank=True) 
    image = models.URLField(default="https://cdn.shopify.com/s/files/1/1132/3108/files/NZ_corner_400x.jpg?v=1603743748")
    def __str__(self):
        return f"{self.username}"


class Destination(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100, null=True, blank=True) 
    image = models.URLField(null=True, blank=True)
    def __str__(self):
        return f"{self.title}"


class Food(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100, null=True, blank=True) 
    image = models.URLField(null=True, blank=True)
    def __str__(self):
        return f"{self.title}"


class Event(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(default=timezone.now)
    location = models.CharField(max_length=100, null=True, blank=True) 
    image = models.URLField(null=True, blank=True)
    def __str__(self):
        return f"{self.title}"


class Blog(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    # description = models.TextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date_created = models.DateField(default=timezone.now) 
    image = models.URLField(null=True, blank=True)
    def __str__(self):
        return f"{self.title}"

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
