from django.db import models

# Create your models here.
class personas(models.Model):
    name = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
