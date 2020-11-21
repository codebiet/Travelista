from django.urls import path
from Places import views

urlpatterns = [
    path('', views.index)
]