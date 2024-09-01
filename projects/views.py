from django.shortcuts import render

# Create your views here.
def projectsView(request):
    context = {
        'title': 'Proyectos'
    }
    return render(request, 'projects.html', context)