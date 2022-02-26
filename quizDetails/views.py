from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import QuizSerializer
from django.db.models import Q
from departmentDetails.models import Level
from .models import Quiz

@api_view(['GET'])
def getAllQuiz(request):
    """
    This endpoint will query out all the course data.
    """
    quizes = Quiz.objects.all()
    serialize = QuizSerializer(quizes, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def get100Quiz(request):
    """
    This endpoint will query out all 100 courses.
    """
    level = Level.objects.get(pk=1)
    quizes = Quiz.objects.filter(level=level)
    serialize = QuizSerializer(quizes, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def get200Quiz(request):
    """
    This endpoint will query out all 200 courses.
    """
    level = Level.objects.get(pk=2)
    quizes = Quiz.objects.filter(level=level)
    serialize = QuizSerializer(quizes, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def get300Quiz(request):
    """
    This endpoint will query out all 300 courses.
    """
    level = Level.objects.get(pk=3)
    quizes = Quiz.objects.filter(level=level)
    serialize = QuizSerializer(quizes, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def get400Quiz(request):
    """
    This endpoint will query out all 400 courses.
    """
    level = Level.objects.get(pk=4)
    quizes = Quiz.objects.filter(level=level)
    serialize = QuizSerializer(quizes, many=True)
    return Response(serialize.data)

@api_view(["GET"])
def getQuiz(request, detail_pk, slug=None):
    """
    This endpoint will query out the associated course provided by 
    the id and slug(quiz slug) respectively.
    """
    try:
        quiz = Quiz.objects.get(
            Q(id=detail_pk) & Q(slug__iexact=slug) )
        serialize = QuizSerializer(quiz, many=False)
        return Response(serialize.data)
    except Quiz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def courseSubject(request, slug=None, course_subject=None):
    """
        This will bring out all the queries related 
        to quizes under Biology, 100. 
        WHERE(100/BIOLOGY) is the slug(level slug) and course_subject respectively,
        the slug and the course_subject can change.

    """

    # Updating this to pk instead of slug in future
    level = Level.objects.get(name=slug)
    course_details = Quiz.objects.filter(
                    course_subject__iexact=course_subject
                    ).filter(
                level=level.pk
            ).order_by("course_code")
    # iexact in the attribute field will match the same format being caps or not.
    # more like course_name.lower() or upper() == course_name

    serialize = QuizSerializer(course_details, many=True)
    return Response(serialize.data)



# NB will be querying out quizes based of semester