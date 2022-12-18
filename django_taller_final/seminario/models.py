from django.db import models

# Create your models here.
class Seminario(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    telefono=models.CharField(max_length=10, null=False)
    fecha=models.DateField(null=False)
    inscripcion=models.CharField(null=False, max_length=50)
    institucion=models.ForeignKey('Institucion', on_delete=models.CASCADE)
    hora=models.TimeField(null=True)
    observacion=models.CharField(max_length=50,)
        
    
    ESTADO_CHOICES=[
        ("d",'Disponible'),
        ("r",'Reservado'),
        ("c",'Completado'),
        ("a",'Anulado'),
    ]
    estado_de_seminario=models.CharField(max_length=2, choices=ESTADO_CHOICES, default="d")
    
    
class Institucion (models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.nombre
    
    
    