from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, permissions

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Comment
from .serializers import CommentModelSerializer







class AddCommentRelatedToUserApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request: Request):
        comment_serializer: CommentModelSerializer = CommentModelSerializer(request.data)
        if (comment_serializer.is_valid()):
            comment_serializer.save(user=request.user)
            return Response(
                comment_serializer.data,
                status=status.HTTP_201_CREATED
            )
            
        return Response(
            comment_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
        
        
        
        





class ListSpecificUserCommentsApiView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request: Request, username: str) -> Response:
        try:
            user: User = User.objects.get(username=username)
        
        except User.DoesNotExist:
            return Response(
                {'error': 'User not Found'},
                status=status.HTTP_404_NOT_FOUND,
            )
            
        comments: Comment = Comment.objects.filter(user=user)
        serialized_comments: CommentModelSerializer = CommentModelSerializer(comments, many=True)
        
        return Response(
            data=serialized_comments.data, 
            status=status.HTTP_302_FOUND,
        )   











class UpdateCommentRelatedToUserApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def put(self, request: Request, pk: int) -> Response:
        try:
            comment: Comment = Comment.objects.get(
                pk=pk,
                user=request.user,
            )
            
        except Comment.DoesNotExist:
            return Response(
                {'error': 'Comment not found or Owned by User'},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        comment_serializer: CommentModelSerializer = CommentModelSerializer(
            comment,
            data=request.data,
        )
        
        if (comment_serializer.is_valid()):
            comment_serializer.save()
            return Response(
                comment_serializer.data,
                status=status.HTTP_200_OK
            )
        
        return Response(
            comment_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )








class DeleteCommentRelatedToUserApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def delete(self, request: Request, comment_id: int) -> Response:
        comment = get_object_or_404(
            klass=Comment,
            id=comment_id,
        )
            
        if (comment.user != request.user):
            return Response(
                {"error": "You don't have permission to delete a Comment"},
                status=status.HTTP_403_FORBIDDEN,
            )
        
        comment.delete()
        
        return Response(
            {'message': 'Comment Deleted Successfully'},
            status=status.HTTP_204_NO_CONTENT,
        )