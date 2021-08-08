from .models import Anime
# Create your views here.
from rest_framework import permissions
from .serializers import AnimeSerializer,UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


class AnimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [permissions.AllowAny]
    
    #filter by user
    def get_queryset(self):
        
        queryset = Anime.objects.all().filter(user=self.request.user)
        return queryset


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
