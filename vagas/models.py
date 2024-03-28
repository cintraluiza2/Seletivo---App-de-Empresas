from django.db import models
from empresa.models import Vagas

class Tarefa(models.Model):
    choices_prioridade = (
        ('B', 'Baixa'),
        ('A', 'Alta'),
        ('U', 'Urgente')
    )
    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    prioridade = models.CharField(max_length=1, choices=choices_prioridade)
    data = models.DateField()
    realizada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Emails(models.Model):
    vaga = models.ForeignKey(Vagas, on_delete=models.DO_NOTHING)
    assunto = models.CharField(max_length=100)
    corpo = models.TextField()
    enviado = models.BooleanField()

    def __str__(self):
        return self.assunto
