
from .serializers import QuizSerializer
from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework import generics
from .models import Quiz
from django.db.models import Q


class QuizListViewAPIView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizLevelAPIView(APIView):

    def get(self, request, level_name):
        quiz_level = get_list_or_404(Quiz, level__name__iexact=level_name)
        if quiz_level:
            serialize = QuizSerializer(quiz_level, many=True)
            return Response(serialize.data)
        return Response({'message': HTTP_404_NOT_FOUND})

# NB will be querying out quizes based of semester


class QuizCourseAPIView(APIView):

    def get(self, request, level_name, course_subject):
        quiz_course = Quiz.objects.filter( 
            Q(level__name__iexact=level_name) & Q(course_subject__iexact=course_subject)
        )
        if quiz_course.exists():
            serialzer = QuizSerializer(quiz_course, many=True)
            return Response(serialzer.data)
        return Response({'message': HTTP_404_NOT_FOUND})


quiz_list = QuizListViewAPIView()
quizlevel_list = QuizLevelAPIView()
quizcourse_list = QuizCourseAPIView()