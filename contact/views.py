from django.shortcuts import render


# Create your views here.
def contactView(request):
    context = {"title": "Contáctame"}
    return render(request, "contact.html", context)


def formContactView(request):
    return render(request, "form-contact.html")
