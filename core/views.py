from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            sender_message = form.cleaned_data['message']

            sent = send_mail(
                subject=f"Portfolio Contact from {form.cleaned_data['name']}",
                message=(
                    f"From: {sender_name} ({sender_email})\n\n"
                    f"{sender_message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )

            if sent:
                messages.success(request, 'Message sent successfully!')
                return redirect('contact')
            messages.error(
                request,
                'Failed to send message. Please try again later.'
            )
        
        return render(request, 'core/contact.html', {'form': form})
