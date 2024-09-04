from django.db import models
from django.contrib.auth.models import User
import os
from PIL import Image


# Create your models here.
class Project(models.Model):
    foto = models.ImageField(upload_to="img_projects/")
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    url_video = models.URLField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    is_wide = models.BooleanField(default=False)
    is_large = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} - {self.descripcion}"

    def save(self, *args, **kwargs):
        # Verifica si ya existe el objeto (actualización)
        if self.pk:
            try:
                old_instance = Project.objects.get(pk=self.pk)
                # Si la imagen ha cambiado, elimina la anterior
                if old_instance.foto and self.foto != old_instance.foto:
                    if os.path.isfile(old_instance.foto.path):
                        os.remove(old_instance.foto.path)
            except Project.DoesNotExist:
                pass

        # Llama al método save original primero para asegurar que la imagen se guarda
        super().save(*args, **kwargs)

        # Abre la imagen recién guardada usando PIL
        img = Image.open(self.foto.path)

        # Obtenemos las dimensiones de la imagen
        width, height = img.size

        # Define is_wide como True si la imagen es más ancha que alta
        self.is_wide = width > height

        # Define is_large como True si la imagen es más alta que ancha
        self.is_large = height > width

        # Guarda los cambios después de ajustar is_wide y is_large
        super().save(update_fields=["is_wide", "is_large"])

    def delete(self, *args, **kwargs):
        if self.foto:
            if os.path.isfile(self.foto.path):
                os.remove(self.foto.path)
        super().delete(*args, **kwargs)
