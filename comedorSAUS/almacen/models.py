from django.db import models

TIPO_INSUMO = {
    ("","-----------"),
    ("1","Alimento"),
    ("2","Limpieza"),
}

UNIDADES_DE_MEDIDA = (
        ('KG', 'Kilogramos'),
        ('LT', 'Litros'),
        ('UN', 'Unidades'),
    )

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.SmallIntegerField("Cantidad")
    tipo_isumo = models.CharField(max_length=1, choices=TIPO_INSUMO)
    unidad_de_medida = models.CharField(max_length=2, choices=UNIDADES_DE_MEDIDA)

    def __str__(self):
        return f"{self.nombre}-{self.stock}-{self.unidad_de_medida}"