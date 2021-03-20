from django.urls import path
from . import views
urlpatterns = [
    path('',views.QuizView.as_view()),
    path('info',views.quiz_info)
]