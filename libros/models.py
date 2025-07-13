from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Clasificacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    clasificacion = models.ForeignKey('Clasificacion', on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='libros_pdfs/', null=True, blank=True)  # Aquí está el campo pdf

    def __str__(self):
        return self.titulo
