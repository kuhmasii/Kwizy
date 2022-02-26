from django.urls import path
from .import views

urlpatterns = [
    path("", views.getAllQuiz),
    path("100/",views.get100Quiz),
    path("200/",views.get200Quiz),
    path("300/",views.get300Quiz),
    path("400/",views.get400Quiz),
    path("detail/<int:detail_pk>/<slug:slug>/", views.getQuiz),
    path("<slug:slug>/<str:course_subject>/", views.courseSubject)
]
