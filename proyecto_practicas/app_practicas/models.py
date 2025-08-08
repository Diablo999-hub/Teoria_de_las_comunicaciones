from django.db import models


# Create your models here.
class Practicas(models.Model):
    nombre = models.CharField(max_length=200)
    objetivo = models.TextField()
    contenido_html = models.TextField()

    def __srt__(self):
        return self.nombre
