from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from qv1.models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer
from rest_framework import generics

# class Quiz1(APIView):

#     def get_object(self):
#         try:
#             return Quiz.objects.all()
#         except Quiz.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND

#     def get(self, request):
#         queryset = self.get_object()
#         serializer = QuizSerializer(queryset, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = QuizSerializer(data=request.data)
#         try:
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)

#         except Exception as e:
#             print('error ', e)
#             return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def delete(self, request):
#         queryset = Quiz.objects.get(id=request.data['id'])
#         queryset.delete()
#         return Response(data=request.data, status=status.HTTP_410_GONE)


#     def put(self, request):
#         # print(request.data)
#         quiz = Quiz.objects.get(id=request.data['id'])
#         serializer = QuizSerializer(quiz, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class Quiz1(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    
    def delete(self, request):
        queryset = Quiz.objects.get(id=request.data['id'])
        queryset.delete()
        return Response(data=request.data, status=status.HTTP_410_GONE)


    def put(self, request):
        # print(request.data)
        quiz = Quiz.objects.get(id=request.data['id'])
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class Question1(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer