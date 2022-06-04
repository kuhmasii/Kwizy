from django.urls import path

from departmentDetails.views import(
    level_list, level_detail)

from quizDetails.views import(
    quiz_list, quizlevel_list, quizcourse_list
)
urlpatterns = [
    path('levels/', level_list.as_view()),
    path("levels/<int:pk>/", level_detail.as_view()),
    path("quizes/", quiz_list.as_view()),
    path("quizes/<str:level_name>/", quizlevel_list.as_view()),
    path("quizes/<str:level_name>/<str:course_subject>/", quizcourse_list.as_view()),

]
