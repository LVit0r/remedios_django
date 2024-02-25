from django.db import models

class Remedio(models.Model):
    nome = models.CharField(max_length = 100)
    mg = models.IntegerField()
    turno = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome
    

class Paciente(models.Model):
    nome = models.CharField(max_length = 100)
    idade = models.IntegerField()
    remedios = models.ManyToManyField(Remedio)

    def __str__(self):
        return self.nome