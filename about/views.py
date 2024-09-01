from django.shortcuts import render

# Create your views here.
def aboutView(request):
    context = {
        'title': '¿Quién soy?'
    }
    return render(request, 'about.html', context)