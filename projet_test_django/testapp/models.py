from django.db import models

# Create your models here.
class Groupe(models.Model):
    nom = models.fields.CharField(max_length=100)
