from django.urls import path
from Places import views

urlpatterns = [
    path('', views.index),
    path('city', views.city),
    path('places_to_visit/<str:city_name>', views.places_to_visit, name='places_to_visit'),
    path('food/<str:city_name>', views.food, name='food')
]