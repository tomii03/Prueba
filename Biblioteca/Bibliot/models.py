from django.db import models

# Create your models here.

class Autor (models.Model):
    nombre = models.CharField(max_length = 20)
    def __str__(self):
        return str (self.nombre)

class Libro (models.Model):
    titulo = models.CharField(max_length = 20)
    editorial = models.CharField(max_length = 20)
    paginas = models.IntegerField()
    autor = models.ForeignKey('Autor', on_delete = models.CASCADE, null = False)
    def __str__(self):
        return str (self.titulo)


class Ejemplar (models.Model):
    localiz = models.CharField(max_length = 20)
    libro = models.ForeignKey('Libro', on_delete= models.CASCADE, null = False)
    def __str__(self):
        return str (self.localiz + "" + self.libro.nombre)


class Usuario (models.Model):
    nombre = models.CharField(max_length = 30, null = False)
    telefono = models.CharField(max_length = 10, null = False)
    direccion = models.CharField(max_length = 30, null = False)
    ejemplares = models.ManyToManyField(Ejemplar)
    def __str__(self):
        return str (self.nombre)