from rest_framework import generics
from app.models import Category,CategoryMinor,Location,Event
from app.api.serializers import CategorySerializer,CategoryMinorSerializer,LocationSerializer,EventSerializer

class EventListView(generics.ListCreateAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class CategoryListView(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class CategoryMinorListView(generics.ListCreateAPIView):
  queryset = CategoryMinor.objects.all()
  serializer_class = CategoryMinorSerializer

class CategoryMinorDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = CategoryMinor.objects.all()
  serializer_class = CategoryMinorSerializer

class LocationListView(generics.ListCreateAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer
