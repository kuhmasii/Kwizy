from django.shortcuts import render
from questionDetails.models import Question
from quizDetails.models import Quiz
from .serializers import QuestionSerializer
from django.db.models import Q

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

@api_view(["GET"])
def quizQuestion(request, quiz_pk, quiz_slug:str):
    """
        This endpoint queries out the questions of a selected course from
        the modal dialogue.
    """
    quiz = Quiz.objects.get(
            Q(id=quiz_pk) & Q(slug__iexact=quiz_slug) )
    ques_image, questions, question_image = '', [], []

    for question in quiz.get_questions():
        if (ques_image := question.questionPicUrl):
            pass
        answers = []
        ans_image = []
        for ans in question.get_ans():
            if ans.AnswerPicUrl:
                ans_image.append(ans.AnswerPicUrl)
            answers.append(ans.answer_text)
        questions.append({str(question) : answers})

        question_image.append(
            {
                'question image':ques_image,
                "answer image": ans_image
            }
        )
    data = {
        'questions': questions, 
        'question-image':question_image, 
        'time':quiz.time
    }
    return Response(data)