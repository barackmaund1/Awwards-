from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView
# Create your views here.
class PostListView(LoginRequiredMixin,ListView):
    
    context_object_name = 'project'
    ordering = ['-date_posted']