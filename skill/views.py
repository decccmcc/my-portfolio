from django.shortcuts import render
from django.views import View
from .models import Skill

class SkillsView(View):
	"""View to display skills categorized by their category."""
	def get(self, request):
		skills_by_category = {}
		for category_code, category_name in Skill.CATEGORY_CHOICES:
			skills = Skill.objects.filter(category=category_code)
			if skills.exists():
				skills_by_category[category_name] = skills
		
		context = {
			'skills_by_category': skills_by_category,
			'all_skills': Skill.objects.all()
		}
		return render(request, "skill/skills_view.html", context)
