from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProjectsView.as_view(), name='projects'),
]