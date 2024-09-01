from django.shortcuts import render


# Create your views here.
def homeView(request):
    context = {"title": "Inicio"}
    return render(request, "home.html", context)
