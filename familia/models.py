from statistics import mode
from django.db import models

class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    altura = models.FloatField()
    fecha_nacimiento = models.DateField()
    email = models.TextField()

    def calcular_edad(self):
        return self.fecha_nacimiento.year - 2022