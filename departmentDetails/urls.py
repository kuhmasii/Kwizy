from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path("levelapi/levels/", views.getlevels),
    path("levelapi/levels/<int:detail_pk>/",views.getlevel),

    # calling a model class method
    path("levelapi/subjects/", views.get_subject)
]
