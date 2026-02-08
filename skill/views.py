from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

# Create your views here.


class SkillsView(View):
	def get(self, request):
		return render(request, "skill/skills_view.html")
