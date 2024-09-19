from django.contrib.auth import authenticate
from django.contrib.auth.models import User, AbstractUser

from rest_framework import serializers




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        
    def create(self, validated_data):
        user: User = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
    




class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data) -> AbstractUser:
        user = authenticate(
            username=data['username'],
            password=data['password']
        )
        
        if (user is None):
            raise serializers.ValidationError('Invalid Username or Password')
        return user