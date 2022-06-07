from rest_framework import serializers


class QuestionPublicSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    question_text = serializers.CharField(read_only=True)
    question_image = serializers.ImageField(read_only=True)


class QuizPublicSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    course_subject = serializers.CharField(read_only=True)
    course_title = serializers.CharField(read_only=True)
    course_code = serializers.CharField(read_only=True)
    semester = serializers.CharField(read_only=True)
