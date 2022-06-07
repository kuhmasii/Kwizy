from .serializers import LevelSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import Level


class LevelListAPIView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = (AllowAny, )


class LevelDetailAPIView(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    lookup_field = 'pk'
    permission_classes = (AllowAny,)


level_list = LevelListAPIView()
level_detail = LevelDetailAPIView()
