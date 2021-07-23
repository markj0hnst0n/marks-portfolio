from django.shortcuts import render
from .models import Project

def projects(request):
    """ A View to return all projects"""
    projects = Project.objects.all()
    context = {
	    'projects': projects,
    }
    return render(request, 'projects/projects.html', context)