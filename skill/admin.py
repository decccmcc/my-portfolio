from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'featured', 'order']
    list_filter = ['category', 'proficiency', 'featured']
    search_fields = ['name']
    list_editable = ['order', 'featured']
