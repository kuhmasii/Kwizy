from django.urls import path
from .import views

urlpatterns = [
    path("", views.get_all_quiz),
    path("100/",views.get_100_quiz),
    path("200/",views.get_200_quiz),
    path("300/",views.get_300_quiz),
    path("400/",views.get_400_quiz),
    path("detail/<int:quiz_pk>/<slug:quiz_slug>/", views.get_quiz),
    path("<slug:level_slug>/<str:course_subject>/", views.course_subject),
]
