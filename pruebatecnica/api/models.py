from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    nacionalidad = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
   # autors = models.ManyToManyField(Autor)

    def __str__(self):
        return self.nombre

