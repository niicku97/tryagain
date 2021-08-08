from .models import Anime
from rest_framework import serializers
from django.contrib.auth.models import User


class AnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = ['id','user','title', 'status', 'last','url_photo']

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'url')

        