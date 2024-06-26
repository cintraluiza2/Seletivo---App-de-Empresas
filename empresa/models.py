from django.db import models


class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia

class Empresa(models.Model):
    choices_nicho_mercado = (
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design'),
        ('T', 'Tecnologia')
    )
    logo = models.ImageField(upload_to="logo_empresa", null=True)
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    tecnologias = models.ManyToManyField(Tecnologias)
    endereco = models.CharField(max_length=30)
    caracteristica_empresa = models.TextField()
    nicho_mercado = models.CharField(max_length=4, choices=choices_nicho_mercado)

    def __str__(self):
        return self.nome

    def qtd_vagas(self):
        return Vagas.objects.filter(empresa__id=self.id).count()

class Vagas(models.Model):
    choices_experiencia = (
        ('J', 'Junior'),
        ('S', 'Senior'),
        ('P', 'Pleno')
    )
    choices_status = (
        ('A', 'Andamento'),
        ('F', 'Finalizado'),
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico')
    )
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.SET_NULL)
    titulo = models.CharField(max_length=30)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    email = models.EmailField(null=True)
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(Tecnologias, related_name='estudar')

    def progresso(self):
        if self.status == 'I':
            return 20
        elif self.status == 'C':
            return 40
        elif self.status == 'E':
            return 60
        elif self.status == 'D':
            return 70
        elif self.status == 'A':
            return 80
        elif self.status == 'F':
            return 100

    def __str__(self):
        return self.titulo
