from django.urls import path
from . import views


urlpatterns = [
    path('questions/', views.getquestions),
    path('questions/<int:quiz_pk>/<slug:quiz_slug>/', views.quiz_question),
]
