from django.db import models

# Create your models here.


class Acesso(models.Model):
    nome = models.CharField(max_length=50, null=False)
    validade = models.DateField(blank=False)

    def __str__(self):
        return self.nome
