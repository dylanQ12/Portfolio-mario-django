from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Project

# Vista de proyectos.
def projectsView(request):
    projects_list = Project.objects.all()
    paginator = Paginator(projects_list, 9)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"title": "Proyectos", "projects": page_obj}
    return render(request, "projects.html", context)
