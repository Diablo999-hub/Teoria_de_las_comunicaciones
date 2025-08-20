from django.db import models
from django.utils.text import slugify

class Practica(models.Model):
    titulo = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    objetivo = models.CharField(max_length=255)
    contenido_html = models.TextField(help_text="Escribe HTML libre (puedes usar <h2>, <p>, <img>, etc.).")

    class Meta:
        ordering = ['titulo']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)[:170]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

