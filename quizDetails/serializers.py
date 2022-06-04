from rest_framework import serializers
from quizDetails.models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'level',
            'id',
            'course_subject',
            'course_title',
            'course_code',
            'semester',
            'section',
            'quiz_slug',
            'number_of_question',
            'time',
            'required_score_to_pass',
        )
