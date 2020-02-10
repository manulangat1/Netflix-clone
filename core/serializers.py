from rest_framework import serializers

from .models import PlayList,Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
class PlayListSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    class Meta:
        model = PlayList
        fields = (
            'id',
            'name',
            'movies'
        )
    def get_movies(self,obj):
        return MovieSerializer(obj.movies.all(),many=True).data