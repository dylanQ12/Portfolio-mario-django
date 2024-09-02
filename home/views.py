from django.shortcuts import render
from projects.models import Project


# Create your views here.
def homeView(request):
    projects = Project.objects.all()[:8]
    context = {
        "title": "Inicio", 
        "projects": projects
    }
    return render(request, "home.html", context)
