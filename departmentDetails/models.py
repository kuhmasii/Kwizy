from django.db import models
from enum import Enum


class RoleEnum(Enum):
    FIRST_YEAR = "100"
    SECOND_YEAR = "200"
    THIRD_YEAR = "300"
    FOURTH_YEAR = "400"

    def __str__(self):
        return self.value


class Level(models.Model):
    name = models.CharField(max_length=20, choices=[
                            (tag.name, tag.value) for tag in RoleEnum])
    slug_name = models.SlugField(max_length=3)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_subject(self):
        # this is reversed relationship query
        all_ = self.quiz_course_level.all()
        # making sure we don't have duplicates
        all_courses = set([x.course_subject.upper() for x in all_])

        return all_courses
