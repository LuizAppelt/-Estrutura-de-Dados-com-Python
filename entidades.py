# entidades.py

# Classe basica para as estruturas de dados
class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

# MClasse do Cliente
class Cliente:
    def __init__(self, id_cliente, nome):
        self.id = id_cliente
        self.nome = nome

# classe do Produto
class Produto:
    def __init__(self, id_produto, nome, quantidade, preco):
        self.id = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

# classe da Venda
class Venda:
    def __init__(self, id_venda, id_cliente, id_produto, quantidade, valor_total):
        self.id = id_venda
        self.id_cliente = id_cliente
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.valor_total = valor_total