from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
User = get_user_model()
# Create your models here.

class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
class Profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(default=0)

    def __str__(self):
        return self.user.username
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
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
class Category(BaseModel):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name