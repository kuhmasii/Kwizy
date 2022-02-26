from django.shortcuts import render
from questionDetails.models import Question
from .serializers import QuestionSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET"])
def getQuestions(request):
    """
        This endpoint returns all question data.
    """
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)