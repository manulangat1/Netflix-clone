from django.contrib import admin

# Register your models here.
from .models import Movie,PlayList
admin.site.register(Movie)
admin.site.register(PlayList)