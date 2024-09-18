from django.contrib.auth.models import User

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