from quizDetails.models import Quiz
from rest_framework import serializers
from .publicserializers import LevelPublicSerializer


class QuizSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='quizdetails-detail', lookup_field='pk')
    level = LevelPublicSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = (
            'level',
            'pk',
            'url',
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


class QuizSerializerSecondary(serializers.ModelSerializer):
    level = LevelPublicSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = (
            'level',
            'pk',
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
