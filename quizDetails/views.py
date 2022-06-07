from .models import Quiz
from django.db.models import Q
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_404_NOT_FOUND
from .serializers import QuizSerializer, QuizSerializerSecondary


class QuizListAPIView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (AllowAny,)


class QuizDetailAPIView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'pk'


class QuizLevelAPIView(APIView):
    # permission_classes = (AllowAny,)

    def get(self, request, level_name):
        quiz_level = Quiz.objects.filter(level__name__iexact=level_name)
        if quiz_level.exists():
            serialize = QuizSerializerSecondary(quiz_level, many=True)
            return Response(serialize.data)
        return Response({'message': HTTP_404_NOT_FOUND})

# NB will be querying out quizes based of semester


class QuizCourseAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, level_name, course_subject):
        quiz_course = Quiz.objects.filter(
            Q(level__name__iexact=level_name) & Q(
                course_subject__iexact=course_subject)
        )
        if quiz_course.exists():
            serialzer = QuizSerializerSecondary(quiz_course, many=True)
            return Response(serialzer.data)
        return Response({'message': HTTP_404_NOT_FOUND})


quiz_list = QuizListAPIView()
quiz_detail = QuizDetailAPIView()
quizlevel_list = QuizLevelAPIView()
quizcourse_list = QuizCourseAPIView()
