from django.shortcuts import render

# Create your views here.
def index(request):
    """ A View to return the homepage"""
    
    return render(request, 'home/index.html')