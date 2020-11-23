from django.urls import path
from Places import views

urlpatterns = [
    path('', views.index),
    path('places_to_visit', views.places_to_visit)
]