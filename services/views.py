from django.shortcuts import render


# Create your views here.
def servicesView(request):
    context = {"title": "Servicios"}
    return render(request, "services.html", context)


def serviceDetailView(request):
    context = {"title": "Detalle de Servicio"}
    return render(request, "service-detail.html", context)


