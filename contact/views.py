from django.shortcuts import render
from .models import Contact
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def contactView(request):
    context = {"title": "Contáctame"}
    return render(request, "contact.html", context)


@csrf_exempt
def formContactView(request):
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        if nombre and apellido and email and mensaje:
            #full_name = f"{nombre} {apellido}"
            contact_item = Contact(nombre=nombre, apellido=apellido ,email=email, mensaje=mensaje)
            contact_item.save()
            return JsonResponse({"success": True, "redirect_url": "/contact/"})
        
        return JsonResponse({"success": False, "error": "Missing fields"})
    
    return render(request, "form/form-contact.html")
