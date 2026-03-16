# estruturas.py
from entidades import Nodo

def LimparTerminal():
    pass

# Lista Encadeada: Usada para Produtos e Clientes
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir(self, dado):
        novo_nodo = Nodo(dado)
        if self.cabeca is None:
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo
            
    def editar_por_id(self, id_busca, novo_nome=None, novo_preco=None):
        objeto_encontrado = self.buscar_por_id(id_busca)
        
        if objeto_encontrado is not None:
            # Se um novo nome foi passado, atualiza
            if novo_nome is not None and novo_nome != "":
                objeto_encontrado.nome = novo_nome
                
            # Se um novo preco foi passado (e o objeto for um Produto), atualiza
            if novo_preco is not None:
                # hasattr verifica se o objeto tem o atributo 'preco' (ou seja, se e um produto)
                if hasattr(objeto_encontrado, 'preco') and novo_preco > 0:
                    objeto_encontrado.preco = novo_preco
                    
            return True # Retorna True indicando que a edicao deu certo
            
        return False # Retorna False se nao achou o ID

    def buscar_por_id(self, id_busca):
        atual = self.cabeca
        while atual is not None:
            if str(atual.dado.id) == str(id_busca):
                return atual.dado
            atual = atual.proximo
        return None
        
    def buscar_por_nome(self, nome_busca):
        atual = self.cabeca
        resultados = []
        while atual is not None:
            # Transforma em minusculo para facilitar a busca
            if nome_busca.lower() in atual.dado.nome.lower():
                resultados.append(atual.dado)
            atual = atual.proximo
        return resultados

    def remover_por_id(self, id_remover):
        atual = self.cabeca
        anterior = None
        while atual is not None:
            if str(atual.dado.id) == str(id_remover):
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def listar_todos(self):
        lista = []
        atual = self.cabeca
        while atual is not None:
            lista.append(atual.dado)
            atual = atual.proximo
        return lista

# Fila: Usada para Vendas (O primeiro a entrar e o primeiro a sair - FIFO)
class Fila:
    def __init__(self):
        self.frente = None
        self.tras = None

    def enfileirar(self, dado):
        novo_nodo = Nodo(dado)
        if self.tras is None:
            self.frente = novo_nodo
            self.tras = novo_nodo
        else:
            self.tras.proximo = novo_nodo
            self.tras = novo_nodo

    def listar_todos(self):
        lista = []
        atual = self.frente
        while atual is not None:
            lista.append(atual.dado)
            atual = atual.proximo
        return lista

    # Metodo extra para ajudar a desfazer a ultima venda (tira do final da fila)
    def remover_ultimo(self):
        if self.frente is None:
            return
        if self.frente == self.tras:
            self.frente = None
            self.tras = None
            return
        atual = self.frente
        while atual.proximo != self.tras:
            atual = atual.proximo
        atual.proximo = None
        self.tras = atual

# Pilha: Usada para o Historico (O ultimo a entrar e o primeiro a sair - LIFO)
class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar(self, dado):
        novo_nodo = Nodo(dado)
        novo_nodo.proximo = self.topo
        self.topo = novo_nodo

    def desempilhar(self):
        if self.topo is None:
            return None
        dado = self.topo.dado
        self.topo = self.topo.proximo
        return dado