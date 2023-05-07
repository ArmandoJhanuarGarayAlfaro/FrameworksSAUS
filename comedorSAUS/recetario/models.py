from django.db import models
from .validadores import imagen_validador


class Receta(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=240)
    hora = models.SmallIntegerField('Hora(s)')
    minuto = models.SmallIntegerField('Minuto(s)')
    ingredientes = models.TextField(blank=True, null=True)
    instrucciones = models.TextField(blank=True, null=True)
    imagen = models.ImageField('Foto de perfil', upload_to='img_recetas', blank=True, null=True, validators=[imagen_validador])

    def __str__(self):
        return f"{self.nombre}-{self.descripcion}-{self.imagen}"
