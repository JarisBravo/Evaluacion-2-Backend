from random import choices
from django.db import models

socio=[
    ('VIGENTE','VIGENTE'),
    ('SUSPENDIDO','SUSPENDIDO'),
    ('RETIRADO','RETIRADO'),
]
# Create your models here.
class Socio(models.Model):
    nombresocio=models.CharField(max_length=50)
    fechaincorporacion = models.IntegerField()
    añodenacimiento = models.IntegerField()
    telefono=models.IntegerField()
    correoelectronico=models.EmailField()
    estado=models.CharField( 
        max_length=20,
        null=False, blank=False,
        choices=socio)
    sexo=models.CharField(max_length=200)
    
    def __str__(self):
        return self
