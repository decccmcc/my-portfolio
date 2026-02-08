from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Project

# Create your views here.


class ProjectsView(View):
	def get(self, request):
		projects = Project.objects.all()
		context = {"projects": projects}

		return render(request, "project/projects_view.html", context)
