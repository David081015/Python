from django.db import models
from personas.models import Domicilio

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL,null=True)