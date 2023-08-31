from .documents import UserDocument
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GetUserSerializer
from rest_framework import status


# Create your views here.

class GetUserView(APIView):
    """
    get all user records from elasticsearch
    """
    
    def get(self, request, format=None):
        users = UserDocument.search().execute()
        serializer = GetUserSerializer(users, many=True)
        return Response(serializer.data)
    
    

class GetUserDetailView(APIView):
    """
    get user by id from elasticsearch
    """
    
    def get(self, request, id, format=None):
        try:
            user = UserDocument.get(id)
            serializer = GetUserSerializer(user)
            return Response(serializer.data)
        except UserDocument.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
class SearchUserView(APIView):
    """
    Search users by username and email in Elasticsearch
    """

    def get(self, request, format=None):
        search_term = request.query_params.get('search', None)
        
        if not search_term:
            return Response({"detail": "Please provide a search term"}, status=status.HTTP_400_BAD_REQUEST)

        users = UserDocument.search().query(
            "bool",
            should=[
                {"wildcard": {"username": f"*{search_term}*"}},
                {"match": {"email": search_term}}
            ]
        )
        
        serializer = GetUserSerializer(users, many=True)
        return Response(serializer.data)