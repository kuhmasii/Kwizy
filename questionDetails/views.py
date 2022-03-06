from django.shortcuts import render
from questionDetails.models import Question
from quizDetails.models import Quiz
from .serializers import QuestionSerializer
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET"])
def getquestions(request):
    """
        This endpoint returns all question data.
    """
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def quiz_question(request, quiz_pk, quiz_slug:str):
    """
        This endpoint queries out the questions of a selected course from
        the modal dialogue.
    """
    quiz = Quiz.objects.get(
            Q(id=quiz_pk) & Q(slug__iexact=quiz_slug) )

    questions = []
    for question in quiz.get_questions():
        if question.questionPicUrl or question.question_text:
            quest = (question.question_text, question.questionPicUrl)
        answers = []
        for ans in question.get_ans():
            if ans.answerPicUrl or ans.answer_text:
                ans_image = (ans.answer_text, ans.answerPicUrl)     
            answers.append(ans_image)
        questions.append({str(quest) : answers})
    data = {
        'questions': questions, 
        'time':quiz.time
    }
    return Response(data)   
            