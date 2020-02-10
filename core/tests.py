from django.test import TestCase
from datetime import datetime
from django.utils import timezone
from .models import BaseModel,Movie,PlayList
# Create your tests here.
class BaseTestClass(TestCase):
    updated_at = datetime.now()
    created_at = datetime.now()
    def setUp(self):
        self.updated_a = BaseModel(updated_at='timezone.now')
    def test_can_be_created(self):
        update = self.updated_a.save()
        Bases = BaseModel.objects.all()
        self.assertTrue(len(Bases) > 0)
    def test_instance(self):
        self.assertTrue(isinstance(self.updated_a,BaseModel))
class MovieTestClass(TestCase):
    # def setUp(self):
    #     self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
    def setUp(self):
        self.movie =  Movie(
                movie_id = 'id',
                movie_url = "https://www.youtube.com/watch?v={ res['id']}",
                movie_thumbnail = 'snippet',
                movie_duration = 60,
                movie_title = 'snippet',
            )
        # print(movie)
    def test_instance(self):
        self.assertTrue(isinstance(self.movie,Movie))
    def test_can_save(self):
        movie = self.movie.save()
        Movies = Movie.objects.all()
        self.assertTrue(len(Movies) > 0)
# class PlayListTestClass(TestCase):
#     def setUp(self):
#         self.movie =  Movie(
#                     movie_id = 'id',
#                     movie_url = "https://www.youtube.com/watch?v={ res['id']}",
#                     movie_thumbnail = 'snippet',
#                     movie_duration = 60,
#                     movie_title = 'snippet',
#                 )
#         self.movie.save()
#         self.mas = PlayList(
#             movies.a(self.movies),
#             name="manu"
            
#         )
#     def test_instance(self):
#         self.assertTrue(isinstance(self.mas,PlayList))
