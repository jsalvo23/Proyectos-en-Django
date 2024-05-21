from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)  # Cambiado a CharField
    genero = models.CharField(max_length=50)
    ano_publicacion = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo