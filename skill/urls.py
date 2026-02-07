from . import views
from django.urls import path

urlpatterns = [
	path('', views.SkillsView.as_view(), name='skills'),
]
