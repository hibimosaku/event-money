from rest_framework import serializers
from app.models import Category,Location,Event,CategoryMinor

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = "__all__"

class CategoryMinorSerializer(serializers.ModelSerializer):
  class Meta:
    model = CategoryMinor
    fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = "__all__"

