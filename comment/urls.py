from django.urls import path

from . import views



urlpatterns = [
    path(
        route='comments/add/',
        view=views.AddCommentRelatedApiView.as_view(),
        name='user-add-comment',
    ),
    path(
        route='comments/<int:pk>/',
        view=views.UpdateCommentRelatedToUserApiView.as_view(),
        name='user-update-comment',
    ),
    path(
        route='comments/<str:username>/',
        view=views.ListSpecificUserCommentsApiView.as_view(),
        name='user-comments',
    ),
    path(
        route='comments/delete/<int:comment_id>/',
        view=views.DeleteCommentRelatedToUserApiView.as_view(),
        name='user-delete-comment'
    ),
]