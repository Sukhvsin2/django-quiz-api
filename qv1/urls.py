from django.urls import path
from .views import Quiz1

urlpatterns = [
    path('', Quiz1.as_view(), name="Quiz1")
]
