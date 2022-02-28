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
    This endpoint will query out all the courses.
    """
    quizes = Quiz.objects.all()
    serialize = QuizSerializer(quizes, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def get100Quiz(request):
    """
    This endpoint will query out all 100 level courses.
    """
    try:
        level = Level.objects.get(pk=1)
        quizes = Quiz.objects.filter(level=level)
        serialize = QuizSerializer(quizes, many=True)
        return Response(serialize.data)
    except Level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get200Quiz(request):
    """
    This endpoint will query out all 200 level courses.
    """
    try:
        level = Level.objects.get(pk=2)
        quizes = Quiz.objects.filter(level=level)
        serialize = QuizSerializer(quizes, many=True)
        return Response(serialize.data)
    except Level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get300Quiz(request):
    """
    This endpoint will query out all 300 level courses.
    """
    try:
        level = Level.objects.get(pk=3)
        quizes = Quiz.objects.filter(level=level)
        serialize = QuizSerializer(quizes, many=True)
        return Response(serialize.data)
    except Level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get400Quiz(request):
    """
    This endpoint will query out all 400 level courses.
    """
    try:
        level = Level.objects.get(pk=4)
        quizes = Quiz.objects.filter(level=level)
        serialize = QuizSerializer(quizes, many=True)
        return Response(serialize.data)
    except Level.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def getQuiz(request, quiz_pk, quiz_slug:str):
    """
    This endpoint will query out the associated course provided by 
    the id(id) and slug(quiz-slug) respectively.
    """
    try:
        quiz = Quiz.objects.get(
            Q(id=quiz_pk) & Q(slug__iexact=quiz_slug) )
        serialize = QuizSerializer(quiz, many=False)
        return Response(serialize.data)
    except Quiz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def courseSubject(request, level_slug:str, course_subject:str):
    """
        This endpoint will query out all the courses related 
        to the quiz under the subject and the level eg(Biology, 100). 
        WHERE(100/BIOLOGY) is the slug(level-slug) and (course_subject) respectively,
        the slug and the course_subject can change.
    """
    # Updating this to pk instead of slug in future
    level = Level.objects.get(name=level_slug)
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