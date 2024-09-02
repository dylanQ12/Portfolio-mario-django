from django.contrib import admin
from .models import Project


# Configuración para el modelo Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "descripcion",
        "fecha_creacion",
        "is_wide",
        "is_large",
        "usuario",
    )  # Campos a mostrar en la tabla
    list_filter = (
        "is_wide",
        "is_large",
        "usuario",
        "fecha_creacion",
    )  # Filtros a mostrar en la barra lateral
    search_fields = ("titulo", "descripcion")  # Campos para buscar
    date_hierarchy = "fecha_creacion"  # Navegación por fecha


admin.site.register(Project, ProjectAdmin)
