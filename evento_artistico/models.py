from django.db import models

class Productores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    cuil = models.IntegerField()

class Musicos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    instrumento = models.CharField(max_length=40)
    cuil = models.IntegerField()

class Tecnicos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    cuil = models.IntegerField()


    