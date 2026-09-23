from django.db import models


class Consola(models.Model):

    TIPOS = [
        ('Xbox', 'Xbox'),
        ('Play 1', 'Play 1'),
        ('Dreamcast', 'Dreamcast'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    cantidad = models.PositiveIntegerField(default=0)
    precio_dia = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre