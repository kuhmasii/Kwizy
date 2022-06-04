from .serializers import LevelSerializer
from rest_framework import generics
from .models import Level


class LevelListAPIView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class LevelDetailAPIView(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    lookup_field = 'pk'


level_list = LevelListAPIView()
level_detail = LevelDetailAPIView()
