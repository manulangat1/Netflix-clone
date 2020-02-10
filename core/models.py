from django.db import models

# Create your models here.
class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
class Movie(BaseModel):
    movie_id = models.CharField(max_length=50)
    movie_url = models.URLField()
    movie_thumbnail = models.CharField(max_length=200)
    movie_duration = models.PositiveIntegerField()
    movie_title = models.CharField(max_length=200)

    def __str__(self):
        return self.movie_title
class PlayList(BaseModel):
    name = models.CharField(max_length=40,null=True,blank=True)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name