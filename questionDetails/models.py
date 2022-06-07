from django.db import models
from django.http import Http404
from quizDetails.models import Quiz


class Question(models.Model):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,
                             related_name="question_quiz")
    question_text = models.CharField(max_length=200, blank=True, null=True)
    question_image = models.ImageField(
        upload_to='question/', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-updated', "-date_created")

    def __str__(self):
        if self.question_text:
            return self.question_text
        return str(self.question_image)

    def get_ans(self):
        answers = self.answer_question.all()
        return answers

    def get_ans_ins(self, ins_pk):
        try:
            ans_ins = self.answer_question.get(pk=ins_pk)
        except self.DoesNotExist:
            raise Http404
        return ans_ins


class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answer_question')
    answer_text = models.CharField(max_length=200, blank=True, null=True)
    ans_image = models.ImageField(upload_to='answer/', blank=True, null=True)
    correct = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.correct)
