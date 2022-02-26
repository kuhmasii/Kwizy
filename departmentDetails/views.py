from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import LevelSerializer
from .models import Level



def index(request):
    return HttpResponse('<H1>add any of these (/docs, /swagger, /redocs)\
        to check documentation</H1>'
    )

@api_view(['GET'])
def getLevels(request):
    """
        This endpoint will query out all the 
        associated levels in the database(100-400)
    """
    data = Level.objects.all()
    serializer = LevelSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLevel(request, detail_pk=None):
    """
        This endpoint will query out a
         level provided by the id.
    """
    data = Level.objects.get(id=detail_pk)
    serializer = LevelSerializer(data)
    return Response(serializer.data)


@api_view(['GET'])
def get_subject(request):
    """
        This endpoint will query out each subjects that
        belong to a particular level.
    """
    levels = Level.objects.all()
    subjects = {}
    for x in levels:
       subjects[x.name] = list(x.get_subject())
    return Response(subjects)
