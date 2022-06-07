from departmentDetails.models import Level
from django.db import models
from enum import Enum


class RoleEnum(Enum):
    FIRST_SEMESTER = "1ST"
    SECOND_SEMESTER = "2ND"

    def __str__(self):
        return self.value


class Quiz(models.Model):

    CHOICES = [(tag.name, tag.value) for tag in RoleEnum]

    level = models.ForeignKey(
        Level, on_delete=models.CASCADE,
        related_name="quiz_course_level"
    )
    course_subject = models.CharField(max_length=100, blank=False,
                                      help_text="Eg: Biology, GST, Biochemistry, Microbiology")
    course_title = models.CharField(max_length=100, blank=False,
                                    help_text='Eg: Immunochemistry, Feasibility studies, Microbial studies')
    course_code = models.CharField(max_length=10, blank=False,
                                   help_text='GST101, BCH301, MCB202, BIO102')
    semester = models.CharField(
        max_length=20, choices=CHOICES, default=CHOICES[0])
    section = models.CharField(max_length=10, blank=True)
    quiz_slug = models.SlugField(max_length=200)

    number_of_question = models.PositiveIntegerField(
        help_text='questions in query')
    time = models.PositiveIntegerField(
        help_text="Duration of the quiz in minutes")
    required_score_to_pass = models.PositiveIntegerField(
        help_text='Passed mark 80%')
    updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("course_subject",)
        verbose_name_plural = "Quizes"

    def __str__(self):
        return f"{self.course_subject}--{self.course_code}"

    def get_questions(self):
        all_questions = self.question_quiz.all()
        # frontend functionality should shuffle and Limit
        # the questions based on number_of_question field
        return all_questions
