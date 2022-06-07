from django.urls import path

from departmentDetails.views import(
    level_list,
    level_detail
)

from quizDetails.views import(
    quiz_list,
    quiz_detail,
    quizlevel_list,
    quizcourse_list
)

from questionDetails.views import(
    question_list,
    questioncourse_list,
    answer_list,
    answercourse_list
)
urlpatterns = [
    path("levels/", level_list.as_view()),
    path("levels/<int:pk>/", level_detail.as_view(),
         name='departmentdetails-detail'),
    path("quizes/", quiz_list.as_view()),
    path("quizes/<int:pk>/", quiz_detail.as_view(), name='quizdetails-detail'),
    path("quizes/level/<str:level_name>/", quizlevel_list.as_view()),
    path("quizes/<str:level_name>/<str:course_subject>/",
         quizcourse_list.as_view()),
    path("questions/", question_list.as_view()),
    path("questions/<int:pk>/", questioncourse_list.as_view()),
    path("answers/", answer_list.as_view()),
    path("answers/<int:pk>/", answercourse_list.as_view()),

]
