from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Service
from django.utils import timezone

# Create your views here.
def servicesView(request):
    services_list = Service.objects.all()
    paginator = Paginator(services_list, 9)  # Muestra 9 servicios por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "title": "Servicios",
        "services": page_obj,
    }
    return render(request, "services.html", context)


def serviceDetailView(request, pk):
    service = get_object_or_404(Service, pk=pk)
    context = {
        "title": f"{service.titulo}",
        "fecha_actual": timezone.now(),
        "service": service,
    }
    return render(request, "service-detail.html", context)
