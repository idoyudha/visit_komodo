from rest_framework import serializers

from .models import Destination, Food, Event, Blog

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination 
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food 
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog 
        fields = '__all__'