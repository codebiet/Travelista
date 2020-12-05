from django.urls import path
from Places import views as Places_views

urlpatterns = [
    path('', Places_views.index, name="index"),
    path('city/', Places_views.city, name="city"),
    path('contact/', Places_views.contact, name="contact"),
    path('about/', Places_views.about, name="about"),
    path('places_to_visit/<str:city_name>/', Places_views.places_to_visit, name='places_to_visit'),
    path('food/<str:city_name>/', Places_views.food, name='food'),
]