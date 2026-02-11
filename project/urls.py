from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProjectsView.as_view(), name='projects'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name='project-detail'),
]