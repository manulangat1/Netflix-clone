from django.shortcuts import render
import requests
from django.http import HttpResponse
from isodate import parse_duration
from .models import Movie
from django.shortcuts import get_object_or_404
# Create your views here.
API_KEY = "AIzaSyDQnTT1O4JNvLBEWTaCj-65aAU4vQd7A_o"
def index(request):
    print(requests)
    api_key = '517b0afadd7811dcb5094755c338f7aa'
    # r = requests.get(f'https://api.themoviedb.org/3/movie/550?api_key={ api_key}')
    r = requests.get(f'https://api.themoviedb.org/3/search/company?api_key={api_key}&query=brooklyn&page=1')
    print(r.json())
    return HttpResponse("Hello wolrd")
def youtube(request):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    search_params = {
        "key":API_KEY,
        'q':'flask',
        'part':'snippet',
        'maxResults':9,
        'type':'video'
    }
    r = requests.get(search_url,params =search_params)
    
    results =r.json()['items']
    video_ids = []
    for result in results:
        video_ids.append(result['id']['videoId'])
    # print(video_ids)
    video_params = {
        "key":API_KEY,
        'id':','.join(video_ids),
        'part':'snippet,contentDetails',
        'maxResults': 9
    }
    r1 = requests.get(video_url,params=video_params)
    res1 =r1.json()['items']
    videos = []
    for res in res1:

        video_data = {
            'id': res['id'],
            'url': f"https://www.youtube.com/watch?v={ res['id']}",
            'thumbnail': res['snippet']['thumbnails']['high']['url'],
            'duration':int(parse_duration(res['contentDetails']['duration']).total_seconds() //60),
            'title':res['snippet']['title'],
        }
        try:
            obj = Movie.objects.get(movie_id = res['id'])
            print(obj)
        except Movie.DoesNotExist:
            print("not there")
            obj = Movie.objects.create(
                movie_id = res['id'],
                movie_url = f"https://www.youtube.com/watch?v={ res['id']}",
                movie_thumbnail = res['snippet']['thumbnails']['high']['url'],
                movie_duration = int(parse_duration(res['contentDetails']['duration']).total_seconds() //60),
                movie_title = res['snippet']['title'],
            )
            obj.save()
        # print(video_data)
        videos.append(video_data)
    print(videos)
    return HttpResponse("cd")
def add_to_playlist(request):
    playlist = []
    movie = Movie.objects.get(movie_id = 'FW1LOP09RM8')
    print(movie.movie_url,movie.movie_title)
    playlist.append(movie)
    # print(playlist)
    return HttpResponse("cd")
def save_youtube():
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    search_params = {
        "key":API_KEY,
        'q':'flask',
        'part':'snippet',
        'maxResults':9,
        'type':'video'
    }
    r = requests.get(search_url,params =search_params)
    
    results =r.json()['items']
    video_ids = []
    for result in results:
        video_ids.append(result['id']['videoId'])
    # print(video_ids)
    video_params = {
        "key":API_KEY,
        'id':','.join(video_ids),
        'part':'snippet,contentDetails',
        'maxResults': 9
    }
    r1 = requests.get(video_url,params=video_params)
    res1 =r1.json()['items']
    videos = []
    for res in res1:

        video_data = {
            'id': res['id'],
            'url': f"https://www.youtube.com/watch?v={ res['id']}",
            'thumbnail': res['snippet']['thumbnails']['high']['url'],
            'duration':int(parse_duration(res['contentDetails']['duration']).total_seconds() //60),
            'title':res['snippet']['title'],
        }
        try:
            obj = Movie.objects.get(movie_id = res['id'])
            print(obj)
        except Movie.DoesNotExist:
            print("not there")
            obj = Movie.objects.create(
                movie_id = res['id'],
                movie_url = f"https://www.youtube.com/watch?v={ res['id']}",
                movie_thumbnail = res['snippet']['thumbnails']['high']['url'],
                movie_duration = int(parse_duration(res['contentDetails']['duration']).total_seconds() //60),
                movie_title = res['snippet']['title'],
            )
            obj.save()
        # print(video_data)
        videos.append(video_data)