from .serializers import MovieSerializer,PlayListSerializer
from .models import PlayList,Movie


from rest_framework import generics
from rest_framework.response import Response

class MovieAPI(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
class PlayListAPI(generics.ListAPIView):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
class MovieCreateAPI(generics.CreateAPIView):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer

    def create(self,request, *args, **kwargs):
        return Response({"hey"})