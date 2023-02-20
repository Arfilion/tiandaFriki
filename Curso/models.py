from django.db import models

# Create your models here.
class videoJuegos(models.Model):
    titulo=models.CharField(max_length=20)
    genero=models.CharField(max_length=20)
    consola=models.CharField(max_length=10)
    releasedate=models.DateField
    completadoAl100=models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

class Peliculas(models.Model):
    titulo=models.CharField(max_length=20)
    genero=models.CharField(max_length=20)
    director=models.CharField(max_length=10)
    releasedate=models.DateField
    vista=models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class miniaturas(models.Model):
    franquicia=models.CharField(max_length=20)
    clase=models.CharField(max_length=20)
    creador=models.CharField(max_length=10)
    pintado=models.BooleanField(default=False)

    def __str__(self):
        return self.franquicia
    
class cartas(models.Model):
    franquicia=models.CharField(max_length=20)
    tipo=models.CharField(max_length=20)
    expansion=models.CharField(max_length=20)
    creador=models.CharField(max_length=10)
    brillante=models.BooleanField(default=False)

    def __str__(self):
        return self.franquicia
   
