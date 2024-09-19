from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth import authenticate

from .serializers import UserSerializer, UserLoginSerializer







class UserRegisterApiView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request: Request) -> Response:
        user_serializer: UserSerializer = UserSerializer(data=request.data)
        if (user_serializer.is_valid()):
            user_serializer.save()
            return Response(
                {"status": "success"},
                status=status.HTTP_201_CREATED,
            )
        
        return Response(
            user_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    
    
    
    
    
    
    
class UserLoginApiView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request: Request) -> Response:
        login_serializer: UserLoginSerializer = UserLoginSerializer(data=request.data)
        if (login_serializer.is_valid()):
            username = login_serializer.validated_data['username']
            password = login_serializer.validated_data['password']
            user = authenticate(
                request=request,
                username=username,
                password=password,
            )
            
            if (user is not None):
                token, created_token = Token.objects.get_or_create(user=user)
                
                return Response(
                    {"token": token.key},
                    status=status.HTTP_200_OK,
                )
            
            else:
                raise AuthenticationFailed('Invalid credentials')
            
        return Response(
            login_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
        
        
        
        
        
        

class UserLogoutApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request: Request) -> Response:
        try:
            token = request.auth
            token.delete()
            
            return Response(
                {"detail": "Successfully logged out"},
                status=status.HTTP_200_OK,
            )

        except Exception as ex:
            return Response(
                {"detail": "Error logging out"},
                status=status.HTTP_400_BAD_REQUEST,
            )