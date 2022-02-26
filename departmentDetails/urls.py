from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path("levelapi/levels/", views.getLevels),
    path("levelapi/levels/<int:detail_pk>/",views.getLevel),

    # calling a model class method
    path("levelapi/subjects/", views.get_subject)
]
