from django.db import models
from bases.models import BaseModel




# Create your models here.

class Luchador(BaseModel):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    # edad = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    alcance = models.DecimalField(max_digits=4, decimal_places=2)
    empates = models.PositiveIntegerField()
    victorias = models.PositiveIntegerField()
    derrotas = models.PositiveIntegerField()
    nacimiento = models.DateField()

    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    
    

