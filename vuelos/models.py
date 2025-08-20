from django.db import models

# Create your models here.

class Vuelo(models.Model):
    NACIONAL = 'Nacional'
    INTERNACIONAL = 'Internacional'
    TIPOS = [
        (NACIONAL, 'Nacional'),
        (INTERNACIONAL, 'Internacional'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices= TIPOS , default='Nacional')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - ${self.precio}"
    