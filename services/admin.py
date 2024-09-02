from django.contrib import admin
from .models import Service


# Configuración para el modelo Service
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "foto",
        "titulo",
        "fecha_creacion",
        "fecha_modificacion",
        "usuario",
    )  # Campos a mostrar en la tabla
    list_filter = ("usuario", "fecha_creacion")  # Filtros a mostrar en la barra lateral
    search_fields = ("titulo", "descripcion")  # Campos para buscar
    date_hierarchy = "fecha_creacion"  # Navegación por fecha


admin.site.register(Service, ServiceAdmin)
