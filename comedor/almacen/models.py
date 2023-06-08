from django.db import models

class TipoInsumo(models.Model):
    nombre = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    numero_lote = models.CharField(max_length=20, blank=True, null=True)
    fecha_caducidad = models.DateField(blank=True, null=True)
    proveedor = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoInsumo, on_delete=models.SET_NULL, null=True, related_name='insumos')

    def __str__(self):
        return self.nombre