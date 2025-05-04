from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('quiz/start/', views.quiz_start, name='quiz_start'),
    path('quiz/submit/', views.quiz_submit, name='quiz_submit'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),
] 