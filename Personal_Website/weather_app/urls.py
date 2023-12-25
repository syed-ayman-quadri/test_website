from django.urls import path
from . import views

urlpatterns = [
    path('weather_app', views.index)
]