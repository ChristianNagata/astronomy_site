from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apod/', views.apod, name='apod'),
    path('MarsRoverPhotos/', views.mars_rover_photos, name='mars_rover_photos'),
    path('MarsRoverPhotos/<int:photo_id>/',
         views.mars_rover_photo, name='mars_rover_photo'),
    path('neows/', views.neows, name='neows'),
]
