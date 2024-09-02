from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellido",
        "email",
        "fecha_envio",
    )  # Campos a mostrar en la tabla
    list_filter = ("fecha_envio",)  # Filtros a mostrar en la barra lateral
    search_fields = ("nombre", "apellido", "email")  # Campos para buscar
    date_hierarchy = "fecha_envio"  # Navegación por fecha


admin.site.register(Contact, ContactAdmin)
