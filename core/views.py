from django.shortcuts import render
from django.views import View
from project.models import Project
from skill.models import Skill
from .forms import ContactForm

class home(View):
    def get(self, request):
        context = {
            'project_count': Project.objects.count(),
            'skill_count': Skill.objects.count(),
        }
        return render(request, 'core/index.html', context)


class contact(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'core/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
        
        return render(request, 'core/contact.html', {'form': form})
