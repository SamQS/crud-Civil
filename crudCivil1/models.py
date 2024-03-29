from django.db import models

# Create your models here.
class proyectosCivil(models.Model):
    codigo=models.BigAutoField(primary_key=True)
    proyecto=models.CharField(max_length=80)
    direccion=models.CharField(max_length=80)
    tipoProyecto=models.TextField() 
    projectManager=models.CharField(max_length=80)
    prioridad=models.PositiveIntegerField() 
    nuevoProyecto=models.CharField(max_length=20)
    propuesta=models.CharField(max_length=20)
    cantidadDias=models.PositiveIntegerField()
    envioPropCliente= models.CharField(max_length=20)
    clienteAprobado= models.CharField(max_length=80)
    proyectoExistente=models.CharField(max_length=20)
    tipoServicio=models.CharField(max_length=100)
    planosCadCliente = models.CharField(max_length=80)
    planosDibus=models.CharField(max_length=80)
    correciones=models.CharField(max_length=80)
    obervaciones=models.TextField() 
    fechaEntrega=models.DateField()
    pc=models.CharField(max_length=80)


    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.codigo, self.proyecto)