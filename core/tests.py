from django.test import TestCase
from datetime import datetime
import json
from .serializers import PlayListSerializer,MovieSerializer
from django.utils import timezone
from .models import BaseModel,Movie,PlayList
import pytest
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
    # return APIClient()
class TestPlaylist(APITestCase):
    def setUp(self):
        self.name = "manu"
        self.movie =  Movie(
                movie_id = 'id',
                movie_url = "https://www.youtube.com/watch?v={ res['id']}",
                movie_thumbnail = 'snippet',
                movie_duration = 60,
                movie_title = 'snippet',
            )
        self.plays = PlayList(name=self.name)
        self.plays.save()
        mov = self.plays.movies.create(movie_id = 'id',
                movie_url = "https://www.youtube.com/watch?v={ res['id']}",
                movie_thumbnail = 'snippet',
                movie_duration = 60,
                movie_title = 'snippet',)
        mov.save()
    @pytest.mark.django_db
    def test_can_get_playlist(self):
        url = reverse('playlist')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_instance(self):
        self.assertTrue(isinstance(self.plays,PlayList))
    def test_save_method(self):
        self.plays.save()
        sd = PlayList.objects.all()
        self.assertTrue(len(sd) > 0)
class MovieTestCase(APITestCase):
    def setUp(self):
        self.movie =  Movie(
            movie_id = 'id',
            movie_url = "https://www.youtube.com/watch?v={ res['id']}",
            movie_thumbnail = 'snippet',
            movie_duration = 60,
            movie_title = 'snippet',
        )
        self.valid_payload = {
            'movie_id' : 'id',
            'movie_url' : "https://www.youtube.com/watch?v=asmvv8w8JY0",
            'movie_thumbnail' : 'snippet',
            'movie_duration' : 60,
            'movie_title' : 'snippet',
        }
        self.invalid_payload = {
            'movie_id' : '',
            'movie_url' : "https://www.youtube.com/watch?v:{ res['id']}",
            'movie_thumbnail' : 'snippet',
            'movie_duration' : 60,
            'movie_title' : 'snippet',
        }
        self.movie.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.movie,Movie))
    def test_can_save(self):
        Mov = Movie.objects.all()
        self.assertTrue(len(Mov)  > 0)
    def test_can_get_all(self):
        url = reverse('movies')
        response = self.client.get(url)
        movies = Movie.objects.all()
        serialiizer = MovieSerializer(movies,many=True)
        self.assertEqual(response.data,serialiizer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_create_movie(self):
        url = reverse('movies_create')
        response = self.client.post(
            url,
            self.valid_payload,
             format='json'
        )
        # serializer = MovieSerializer(instance =data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    """
      testing that invalid data cannot be created 
    """
    def test_create_invalid_puppy(self):
        response = self.client.post(
            reverse('movies_create'),
            self.invalid_payload,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
