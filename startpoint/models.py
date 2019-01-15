from django.db import models


class ConsultaCliente(models.Model):
    nome = models.CharField(max_length= 200)
    cpf = models.CharField(max_length= 15)
    data_nascimento = models.CharField(max_length= 10)
    rua = models.CharField(max_length= 50)
    numero = models.CharField(max_length= 10)
    barrio = models.CharField(max_length= 50)
    cidade = models.CharField(max_length= 50)
    pais = models.CharField(max_length= 100)
    numero_celular = models.CharField(max_length= 20)

    def __str__(self):
        return self.nome



