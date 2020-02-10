from django.urls import path
from .views import index,youtube,add_to_playlist
from .api import MovieAPI,PlayListAPI,MovieCreateAPI

urlpatterns = [
    path('',index),
    path('data/',youtube),
    path('play/',add_to_playlist),
    path('movie/',MovieAPI.as_view()),
    path('movie/create/',MovieCreateAPI.as_view()),
    path('playlist/',PlayListAPI.as_view()),
]
