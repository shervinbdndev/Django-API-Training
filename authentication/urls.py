from django.urls import path

from . import views


urlpatterns = [
    path(
        route='register/',
        view=views.UserRegisterApiView.as_view(),
        name='register-user',
    ),
    path(
        route='login/',
        view=views.UserLoginApiView.as_view(),
        name='login-user',
    ),
    path(
        route='logout/',
        view=views.UserLogoutApiView.as_view(),
        name='logout-user',
    )
]