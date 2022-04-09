from app.api import views
from django.urls import path

urlpatterns = [
  path("event/",views.EventListView.as_view(),name="eventList"),
  path("event/<int:pk>/",views.EventDetailView.as_view(),name="eventDetail"),
  path("category/",views.CategoryListView.as_view(),name="categoryList"),
  path("category/<int:pk>",views.CategoryDetailView.as_view(),name="categoryDetail"),

  path("categoryMinor/",views.CategoryMinorListView.as_view(),name="categoryMinorList"),
  path("categoryMinor/<int:pk>",views.CategoryMinorDetailView.as_view(),name="categoryMinorDetail"),
  path("location/",views.LocationListView.as_view(),name="locationList"),
  path("location/<int:pk>",views.LocationDetailView.as_view(),name="locationDetail"),

]