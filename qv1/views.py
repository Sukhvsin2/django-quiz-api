from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from qv1.models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer
from rest_framework import generics

class Quiz1(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    
    def delete(self, request):
        queryset = Quiz.objects.get(id=request.data['id'])
        queryset.delete()
        return Response(data=request.data, status=status.HTTP_410_GONE)


    def put(self, request):
        quiz = Quiz.objects.get(id=request.data['id'])
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class Question1(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, id, *args, **kwargs):
        questions = Question.objects.filter(quiz_id=id)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)