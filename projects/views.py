from django.shortcuts import render
from .models import Project

# Create your views here.

def projects(request):
    """ A View to return all projects"""
    projects = Project.objects.all()
    context = {
	    'projects': projects,
    }
    return render(request, 'projects/projects.html', context)