from django.db import models
from quizDetails.models import Quiz

class Question(models.Model):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, 
    related_name="question_quiz")
    question_text = models.CharField(max_length=200)
    question_image = models.ImageField(upload_to='question/', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-updated',"-date_created")

    def __str__(self):
        return self.question_text
    
    def get_ans(self):
        return self.answer_question.all()

    def get_ans_ins(self, ins_pk):
        return self.answer_question.get(pk=ins_pk)

class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                    related_name='answer_question')
    answer_text = models.CharField(max_length=200)
    ans_image = models.ImageField(upload_to='answer/', blank=True, null=True)
    correct = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.correct)
