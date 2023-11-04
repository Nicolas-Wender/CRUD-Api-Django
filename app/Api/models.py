from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=800, default="Descrição do produto")
    preco = models.DecimalField(max_digits=4, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    "fazer a parada de escolher em uma seleção"
    CATEGORIAS = [
        ("Eletrônicos", "Eletrônicos"),
        ("Casa e Decoração", "Casa e Decoração"),
        ("Moda", "Moda"),
    ]
    categoria = models.CharField(max_length=16, choices=CATEGORIAS)

    def __str__(self):
        return f"{self.nome} {self.descricao} {self.preco} {self.quantidade} {self.categoria}"