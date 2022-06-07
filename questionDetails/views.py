from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework import generics
from quizDetails.models import Quiz
from rest_framework.views import APIView
from questionDetails.models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerialier
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (AllowAny, )


class AnswerListAPIView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerialier
    permission_classes = (AllowAny, )


class QuestionCourseListAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, pk):
        try:
            questions = Quiz.objects.get(pk=pk).get_questions()
        except Quiz.DoesNotExist():
            return Response(
                {'message': HTTP_404_NOT_FOUND}
            )
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class AnswerCourseListAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, pk):
        try:
            answers = Question.objects.get(pk=pk).get_ans()
        except Question.DoesNotExist():
            return Response(
                {'message': HTTP_404_NOT_FOUND}
            )
        serializer = AnswerSerialier(answers, many=True)
        return Response(serializer.data)


question_list = QuestionListAPIView()
questioncourse_list = QuestionCourseListAPIView()
answer_list = AnswerListAPIView()
answercourse_list = AnswerCourseListAPIView()
