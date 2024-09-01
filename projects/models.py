from django.db import models
from django.contrib.auth.models import User
import os


# Create your models here.
class Project(models.Model):
    foto = models.ImageField(upload_to="img_projects/")
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    url_video = models.URLField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.descripcion}"

    def save(self, *args, **kwargs):
        if self.pk:  # Si el objeto ya existe, es una actualización
            old_instance = Project.objects.get(pk=self.pk)
            if old_instance.foto and self.foto != old_instance.foto:
                if os.path.isfile(old_instance.foto.path):
                    os.remove(old_instance.foto.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.foto:
            if os.path.isfile(self.foto.path):
                os.remove(self.foto.path)
        super().delete(*args, **kwargs)
