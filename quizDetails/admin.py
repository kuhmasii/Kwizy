from django.contrib import admin
from .models import Quiz


class QuizAdmin(admin.ModelAdmin):
    list_display = "course_subject course_title course_code number_of_question".split()
    list_filter = "course_subject course_title course_code semester section number_of_question date_created".split()
    prepopulated_fields = {"slug": ("course_subject", "course_title", "course_code")}


admin.site.register(Quiz, QuizAdmin)