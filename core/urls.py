from django.urls import path
from .views import index,youtube,add_to_playlist

urlpatterns = [
    path('',index),
    path('data/',youtube),
    path('play/',add_to_playlist)
]