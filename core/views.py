from django.shortcuts import render
import requests
from django.http import HttpResponse
from isodate import parse_duration
# Create your views here.
API_KEY = "AIzaSyDQnTT1O4JNvLBEWTaCj-65aAU4vQd7A_o"
def index(request):
    print(requests)
    r = requests.get('https://api.github.com/search/repositories',
params={'q': 'requests+language:python'},)
    # print(r.text)
    json_response = r.json()
    # print(json_response)
    repository = json_response['items'][0]
    print(repository)
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

        # print(video_data)
        videos.append(video_data)
    print(videos)
    return HttpResponse("cd")