from django.db import models

class Level(models.Model):
    STUDENT_LEVEL = [
        ('100', "FIRST YEAR"),
        ('200', "SECOND YEAR"),
        ('300', "THIRD YEAR"),
        ('400', "FOURTH YEAR"),
    ]
    name = models.CharField(max_length=3, choices=STUDENT_LEVEL,
                            blank=False, default='100')
    slug_name = models.SlugField(max_length=3)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_subject(self):
        # this is reversed relationship query
        all_ = self.quiz_course_level.all()
        # trying to get only one instance of the course
        all_courses = set([x.course_subject.upper() for x in all_])
        
        return all_courses
