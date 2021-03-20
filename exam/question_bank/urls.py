from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.ChoiceView.as_view()),
]
