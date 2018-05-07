from django.db import models

# Modelos para actividades .


class Ubicacion(models.Model):
    id = models.AutoField(primary_key=True, default=123)
    Descripcion = models.CharField(max_length=100)
    def __str__(self):#retorna lo que se desea ver de la clase, en este caso es olo la descripcion
        return '%s' % (self.Descripcion)


class Tiposact(models.Model):
    id = models.AutoField(primary_key=True, default=123)
    Nombre = models.CharField(max_length=50)
    def  __str__(self):
        return '%s' % (self.Nombre)

class Empleados(models.Model):
    id = models.AutoField(primary_key=True, default=123)
    Nombre = models.CharField(max_length=50)
    Puesto = models.CharField(max_length=50)
    def  __str__(self):
        return '%s %s' % (self.Nombre,self.Puesto)
class Activity(models.Model):
    Id= models.AutoField(primary_key=True ,default="123", editable=False)
    Nombre = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=100)
    Type = models.ForeignKey(Tiposact,on_delete=models.CASCADE,default='123')
    FechaCreacion = models.IntegerField
    HoraInicial = models.IntegerField
    Duracion = models.IntegerField
    DiasAct = models.CharField(max_length=45)
    Rangoedad = models.CharField(max_length=45)
    Cupo = models.IntegerField
    Ubica = models.ForeignKey(Ubicacion,on_delete=models.CASCADE,default='123')
    Instructor = models.ForeignKey(Empleados,on_delete=models.CASCADE,default='123')
    def  __str__(self):
        return '%s %s ' % (self.Nombre,self.Cupo)


