from rest_framework import serializers

from .models import PlayList,Movie,Profile
from django.contrib.auth import get_user_model
User = get_user_model()

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
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "id",
            "bio",
        )
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     profile = ProfileSerializer()
#     class Meta:
#         model = User
#         depth = 1
#         fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email',
#                   'is_superuser', 'is_staff', 'profile')
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'profile'
        )
    def create(self, validated_data):
        # create user 
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            # etc ...
        )
        profile_data = validated_data.pop('profile')
        print(profile_data)
        profile = Profile.objects.create(
            user = user,
            bio = profile_data['bio']
        )
        profile.save()
        return user