from django.db import models

# Create your models here.


class Ubicacion(models.Model):
    ID = models.AutoField(primary_key=True,default='123')
    Descripcion = models.CharField(max_length=100)
    def __str__(self):
        "Returns the person's full name."
        return '%s' % (self.Descripcion)


class Tiposact(models.Model):
    ID = models.AutoField(primary_key=True,default='123')
    Nombre = models.CharField(max_length=50)
    def  __str__(self):
        "Returns the person's full name."
        return '%s' % (self.Nombre)

class Empleados(models.Model):
    ID = models.AutoField(primary_key=True,default='123')
    Nombre = models.CharField(max_length=50)
    Puesto = models.CharField(max_length=50)
    def  __str__(self):
        "Returns the person's full name."
        return '%s %s' % (self.Nombre,self.Puesto)

class Activity(models.Model):
    ID = models.AutoField(primary_key=True,default='123')
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=100)
    Type = models.ForeignKey(Tiposact,on_delete=models.CASCADE,default='123')
    FechaCreacion = models.IntegerField
    HoraInicial = models.IntegerField
    Duracion = models.IntegerField
    DiasAct = models.CharField(max_length=45)
    Rangoedad = models.CharField(max_length=45)
    Cupo = models.IntegerField
    Ubicacion = models.ForeignKey(Ubicacion,on_delete=models.CASCADE,default='123')
    Instructor = models.ForeignKey(Empleados,on_delete=models.CASCADE,default='123')
    def  __str__(self):
        "Returns the person's full name."
        return '%s %s %s' % (self.Nombre,self.Type,self.Cupo)
