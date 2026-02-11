from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Project

# Create your views here.


class ProjectsView(View):
	def get(self, request):
		projects = Project.objects.all()
		context = {"projects": projects}

		return render(request, "project/projects_view.html", context)


class ProjectDetailView(DetailView):
	"""View to display the details of a single project."""
	model = Project
	template_name = 'project/project_detail.html'
	context_object_name = 'project'
	slug_field = 'slug'
	slug_url_kwarg = 'slug'
	
	# get default context data and add images to the context
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['images'] = self.object.images.all()
		return context
