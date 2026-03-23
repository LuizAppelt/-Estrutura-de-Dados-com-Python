# entidades.py

from dataclasses import dataclass

# Classe básica para estruturas de dados (lista encadeada)
class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __repr__(self):
        return f"Nodo(dado={self.dado})"


# Classe Cliente
@dataclass
class Cliente:
    id: int
    nome: str

    def __post_init__(self):
        if not self.nome:
            raise ValueError("Nome do cliente não pode ser vazio")

    def __repr__(self):
        return f"Cliente(id={self.id}, nome='{self.nome}')"


# Classe Produto
@dataclass
class Produto:
    id: int
    nome: str
    quantidade: int
    preco: float

    def __post_init__(self):
        if self.quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa")
        if self.preco < 0:
            raise ValueError("Preço não pode ser negativo")

    def __repr__(self):
        return (f"Produto(id={self.id}, nome='{self.nome}', "
                f"quantidade={self.quantidade}, preco={self.preco})")


# Classe Venda
@dataclass
class Venda:
    id: int
    id_cliente: int
    id_produto: int
    quantidade: int
    valor_total: float

    def __post_init__(self):
        if self.quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        if self.valor_total < 0:
            raise ValueError("Valor total não pode ser negativo")

    def __repr__(self):
        return (f"Venda(id={self.id}, cliente={self.id_cliente}, "
                f"produto={self.id_produto}, quantidade={self.quantidade}, "
                f"total={self.valor_total})")
