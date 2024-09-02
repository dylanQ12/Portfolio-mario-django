from django.contrib import admin
from .models import Client


# Configuración para el modelo Client
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "foto",
        "nombre",
        "apellido",
        "profesion",
        "empresa",
        "fecha_creacion",
        "fecha_modificacion",
    )  # Campos a mostrar en la tabla
    list_filter = (
        "profesion",
        "empresa",
        "fecha_creacion",
    )  # Filtros a mostrar en la barra lateral
    search_fields = ("nombre", "apellido", "profesion", "empresa")  # Campos para buscar
    date_hierarchy = "fecha_creacion"  # Navegación por fecha


# Register your models here.
admin.site.register(Client, ClientAdmin)
