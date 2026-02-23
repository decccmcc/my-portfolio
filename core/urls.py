from . import views
from django.urls import path

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('contact/', views.contact.as_view(), name='contact'),
]