from .serializers import MovieSerializer,PlayListSerializer,UserSerializer,ProfileSerializer
from .models import PlayList,Movie

from rest_framework import viewsets, mixins, permissions
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()
class MovieAPI(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
class MoviesAPI(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
class PlayListAPI(generics.ListAPIView):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
class MovieCreateAPI(generics.CreateAPIView):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
# class UserList(generics.ListCreateAPIView):
class UserList(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsSameUserAllowEditionOrReadOnly,)
    # permission_classes = (IsAuthenticatedOrWriteOnly,)
    # serializer_class = UserSerializer
    # queryset = User.objects.all()
    # def post(self, request, format=None):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)