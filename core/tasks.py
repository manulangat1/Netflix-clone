from celery.task.schedules import crontab
from celery.decorators import periodic_task
import requests
from django.http import HttpResponse
from isodate import parse_duration
from .models import Movie
from django.shortcuts import get_object_or_404
from celery.utils.log import get_task_logger
from .views import save_youtube
logger = get_task_logger(__name__)
API_KEY = "AIzaSyDQnTT1O4JNvLBEWTaCj-65aAU4vQd7A_o"
@periodic_task(run_every=(crontab(minute='*/1')), name="youtube", ignore_result=True)
def youtube():
    """
    Saves latest image from Flickr
    """
    save_youtube()
    logger.info("Saved image from Flickr")