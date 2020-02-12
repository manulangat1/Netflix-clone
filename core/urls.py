from django.urls import path
from .views import index,youtube,add_to_playlist
from .api import MovieAPI,PlayListAPI,MovieCreateAPI,MoviesAPI,UserList
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserList)

urlpatterns = [
    path('',index),
    path('data/',youtube),
    path('play/',add_to_playlist),
    path('movie/',MovieAPI.as_view(),name='movies'),
    # path('user/',UserList,name='user'),
    path('movies/',MoviesAPI.as_view(),name='movies_create'),
    path('movie/create/',MovieCreateAPI.as_view(),name='movie_create'),
    path('playlist/',PlayListAPI.as_view(),name='playlist'),
]

urlpatterns += router.urls