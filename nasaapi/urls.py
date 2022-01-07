from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('APOD/', views.apod, name='apod'),
    path('MarsRoverPhotos/', views.mars_rover_photos, name='mars_rover_photos'),
]
