from django.urls import path
from . import views


urlpatterns = [
    path('questions/', views.getQuestions),
    path('questions/<int:quiz_pk>/<slug:quiz_slug>/', views.quizQuestion),
]
