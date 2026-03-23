
# 📦 Sistema de Estoque e Vendas em Python

## 📚 Disciplina

**Organização e Abstração na Programação** – Professor: Augusto Ortolan

## 👥 Integrantes

* Gabriel Pasuch Granja – 1138917
* Guilherme Silva – 1133534
* Guilherme Vieira Marques – 1138951
* Luiz Henrique Appelt Weller – 1138930
* Ricardo Trento Werner – 1138812

---

## 📌 Descrição do Projeto

Este projeto implementa um **mini sistema de gerenciamento de estoque e vendas** em Python, totalmente executado via terminal, com **persistência automática de dados** em arquivos `.csv` ou `.txt`.

O sistema permite:

* Cadastro e listagem de clientes;
* Cadastro e controle de produtos em estoque;
* Registro de vendas;
* Consulta de histórico de vendas;
* Desfazer a última operação realizada.

A persistência garante que **nenhuma informação seja perdida** ao encerrar o programa.

---

## 🧠 Conceitos Aplicados

O projeto foi desenvolvido com foco em **aplicação prática** de:

* Programação Orientada a Objetos (POO)
* Estruturas de Dados
* Manipulação de arquivos
* Tratamento de erros
* Organização e modularização de código

---

## 🏗️ Estruturas de Dados Utilizadas

### 🔗 Lista Encadeada

* Armazena **clientes** e **produtos**
* Permite inserção, remoção, busca e listagem
* Implementada manualmente, sem uso de estruturas prontas do Python

### 📥 Fila (FIFO)

* Armazena **vendas realizadas**
* Mantém o registro na ordem em que ocorrem

### 📤 Pilha (LIFO)

* Armazena **histórico de operações**
* Permite desfazer a última ação realizada

---

## 💾 Persistência de Dados

Os dados são armazenados em arquivos locais:

* `clientes.csv` / `clientes.txt`
* `produtos.csv` / `produtos.txt`
* `vendas.csv` / `vendas.txt`

**Funcionamento automático:**

* Ao iniciar, os arquivos são carregados ou criados se não existirem
* Qualquer alteração é salva automaticamente
* Não há necessidade de salvar manualmente

---

## ⚙️ Funcionalidades

1. Cadastrar cliente
2. Listar clientes
3. Cadastrar produto
4. Listar produtos
5. Pesquisar produto
6. Realizar venda
7. Visualizar fila de vendas
8. Desfazer última operação
9. Exibir valor total do estoque
10. Exibir valor total de vendas
11. Exibir clientes e total gasto
12. Sair

---

## 📏 Regras de Negócio

* Cliente deve estar cadastrado para realizar compra
* Produto deve estar cadastrado para venda
* Quantidade e preço devem ser maiores que zero
* Estoque não pode ficar negativo
* Campos obrigatórios não podem estar vazios
* Operações inválidas não alteram os dados

---

## 🛡️ Tratamento de Erros

O sistema lida com:

* Entradas inválidas do usuário
* IDs inexistentes
* Arquivos inexistentes ou corrompidos
* Tentativas de operações inválidas
* Falhas de leitura/escrita de arquivos
* Dados inconsistentes

**Sempre que ocorre um erro:**

* O usuário é informado
* A operação é cancelada
* O sistema continua funcionando normalmente

---

## ▶️ Como Executar

### ✅ Pré-requisitos

* Python 3

### 🚀 Passos

1. Clone o repositório:

```bash
git clone https://github.com/LuizAppelt/Estrutura_de_Dados_com_Python
```

2. Acesse a pasta do projeto:

```bash
cd Estrutura_de_Dados_com_Python
```

3. Execute o sistema:

```bash
python main.py
```

---

## 📁 Estrutura do Projeto

```
📦 projeto
 ┣ 📜 main.py
 ┣ 📜 produto.py
 ┣ 📜 cliente.py
 ┣ 📜 venda.py
 ┣ 📜 lista_encadeada.py
 ┣ 📜 fila.py
 ┣ 📜 pilha.py
 ┣ 📜 clientes.csv
 ┣ 📜 produtos.csv
 ┣ 📜 vendas.csv
 ┗ 📜 README.md
```

---

## 📌 Observações Finais * O sistema é totalmente executado via terminal. * O foco principal é a aplicação prática de estruturas de dados. * O código foi desenvolvido com organização e comentários explicativos. * Todos os integrantes devem contribuir com commits reais no projeto.


