from django.db import models
from bases.models import BaseModel




# Create your models here.

class Luchador(BaseModel):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    pais = models.CharField(max_length=50, null=True, blank=True)
    guardia = models.CharField(max_length=50, null=True, blank=True, default="derecha")
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    alcance = models.DecimalField(max_digits=4, decimal_places=2)
    empates = models.PositiveIntegerField()
    victorias = models.PositiveIntegerField()
    derrotas = models.PositiveIntegerField()
    nacimiento = models.DateField()
    edad = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_totales = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_acertados = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_fallados = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_recibidos = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_encajados = models.PositiveIntegerField(null=True, blank=True, default=0)
    golpes_evitados = models.PositiveIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    
    

