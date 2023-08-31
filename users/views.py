from .documents import UserDocument
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GetUserSerializer


# Create your views here.

class GetUserView(APIView):
    """
    get all user records from elasticsearch
    """
    
    def get(self, request, format=None):
        users = UserDocument.search().execute()
        serializer = GetUserSerializer(users, many=True)
        return Response(serializer.data)