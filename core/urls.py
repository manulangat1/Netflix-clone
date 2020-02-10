from django.urls import path
from .views import index,youtube

urlpatterns = [
    path('',index),
    path('data/',youtube),
]