from django.shortcuts import render
from django.views import View
from project.models import Project
from skill.models import Skill

class home(View):
    def get(self, request):
        context = {
            'project_count': Project.objects.count(),
            'skill_count': Skill.objects.count(),
        }
        return render(request, 'core/index.html', context)
