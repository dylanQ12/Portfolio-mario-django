from django.db import models
import os


# Create your models here.
class Client(models.Model):
    foto = models.ImageField(upload_to="photo_clients/")
    nombre = models.CharField(max_length=200, null=False, blank=False)
    apellido = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=260, null=False, blank=False)
    profesion = models.CharField(max_length=200, null=False, blank=False)
    empresa = models.CharField(max_length=200, null=True, blank=True)
    comentario = models.TextField(null=False, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Profesión: {self.profesion} - Comentario: {self.comentario}"

    def save(self, *args, **kwargs):
        if self.pk:  # Si el objeto ya existe, es una actualización
            old_instance = Client.objects.get(pk=self.pk)
            if old_instance.foto and self.foto != old_instance.foto:
                if os.path.isfile(old_instance.foto.path):
                    os.remove(old_instance.foto.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.foto:
            if os.path.isfile(self.foto.path):
                os.remove(self.foto.path)
        super().delete(*args, **kwargs)
