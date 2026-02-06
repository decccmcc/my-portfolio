from django.shortcuts import render

# Create your views here.
class home(TemplateView):
    template_name = 'index.html'
