from django.http import HttpResponse
from django.views import View

# Create your views here.


class SkillsView(View):
	def get(self, request):
		return HttpResponse("Skills page")
