from django.urls import path
from .views import Quiz1, Question1

urlpatterns = [
    path('quiz/', Quiz1.as_view(), name="Quiz1"),
    path('questions/', Question1.as_view(), name="Question1"),
]
