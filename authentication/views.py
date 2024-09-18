from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.http.request import HttpRequest
from django.contrib.auth import authenticate

from .serializers import UserSerializer






class UserLoginApiView(APIView):
    def post(self, request: HttpRequest) -> Response:
        pass