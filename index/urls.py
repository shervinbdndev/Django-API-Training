from django.urls import path
from . import views

urlpatterns = [
    path(
        route='',
        view=views.IndexView.as_view(),
        name='index',
    )
]