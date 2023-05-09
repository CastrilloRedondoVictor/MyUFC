from django.db import models

from bases.models import BaseModel
from luchadores.models import Luchador


RESULTADOS_CHOICES = [
        ('Rojo', 'Rojo'),
        ('Empate', 'Empate'),
        ('Azul', 'Azul'),
    ]

# Create your models here.

class Combate(BaseModel):
    luchador_rojo = models.ForeignKey(Luchador, on_delete=models.CASCADE, related_name='combates_rojo')
    luchador_azul = models.ForeignKey(Luchador, on_delete=models.CASCADE, related_name='combates_azul')
    fecha = models.DateField()
    round_max = models.PositiveIntegerField()
    resultado = models.CharField(choices=RESULTADOS_CHOICES)
    golpes_rojo = models.PositiveIntegerField()
    golpes_acertados_rojo = models.PositiveIntegerField()
    golpes_fallados_rojo = models.PositiveIntegerField()
    golpes_directos_rojo = models.PositiveIntegerField()
    golpes_crochet_rojo = models.PositiveIntegerField()
    golpes_gancho_rojo = models.PositiveIntegerField()
    golpes_azul = models.PositiveIntegerField()
    golpes_acertados_azul = models.PositiveIntegerField()
    golpes_fallados_azul = models.PositiveIntegerField()
    golpes_directos_azul = models.PositiveIntegerField()
    golpes_crochet_azul = models.PositiveIntegerField()
    golpes_gancho_azul = models.PositiveIntegerField()