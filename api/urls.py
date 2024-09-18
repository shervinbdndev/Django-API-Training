from django.urls import path
from . import views


urlpatterns = [
    path(
        route='users/',
        view=views.ListUsersApiView.as_view(),
        name='users',
    ),
]