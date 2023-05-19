from django.db import models

class teste(models.Model):
    nome = models.CharField(
        max_length= 155
    )
class teste2 (models.Model):
    idade = models.CharField(
        max_length=100
    )
class teste3 (models.Model):
    idade2 = models.CharField(
        max_length=100
    )