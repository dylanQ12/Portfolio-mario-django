from django.db import models


# Create your models here.
class Contact(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=260)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Enviado: {self.fecha_envio} - Mensaje: {self.mensaje}"
