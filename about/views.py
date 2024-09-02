from django.shortcuts import render
from clientes.models import Client

# Create your views here.
def aboutView(request):
    clients = Client.objects.all()
    context = {
        'title': '¿Quién soy?',
        'clients': clients
    }
    return render(request, 'about.html', context)