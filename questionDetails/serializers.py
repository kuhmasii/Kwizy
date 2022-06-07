from rest_framework import serializers
from .publicserializers import QuestionPublicSerializer, QuizPublicSerializer
from questionDetails.models import Answer, Question


class AnswerInlineSerializer(serializers.Serializer):

    pk = serializers.IntegerField(read_only=True)
    answer_text = serializers.CharField(read_only=True)
    ans_image = serializers.ImageField(read_only=True)
    correct = serializers.BooleanField(read_only=True)


class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizPublicSerializer(read_only=True)
    answers = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        fields = (
            'quiz',
            'id',
            'question_text',
            'question_image',
            'updated',
            'date_created',
            'answers'
        )

    def get_answers(self, obj):
        if not hasattr(obj, 'id'):
            return None
        return AnswerInlineSerializer(
            obj.get_ans(), many=True).data


class AnswerSerialier(serializers.ModelSerializer):
    question = QuestionPublicSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = (
            'question',
            'pk',
            "answer_text",
            "ans_image",
            "correct",
            "updated",
            "date_created",
        )
