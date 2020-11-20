from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class Message(APIView):

    def get(self, request):
        return Response(data={'data': 'Class based Get message'}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response(data={'data': 'Class Based Post message'}, status=status.HTTP_200_OK)