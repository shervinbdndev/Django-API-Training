from rest_framework import serializers

from comment.models import Comment




class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user' ,'text', 'rate', 'viewed_by_admin', 'created_at', 'updated_at']