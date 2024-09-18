from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from rest_framework import authentication, permissions





class ListUsersApiView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    
    def get(self, request: HttpRequest) -> Response:
        usernames: list = [f'{user.username}' for user in User.objects.all()]
        
        return Response(usernames)