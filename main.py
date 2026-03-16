# main.py
import os
from entidades import Cliente, Produto, Venda
from estruturas import ListaEncadeada, Fila, Pilha

COR_CADASTRO = '\033[96m'  # Ciano
COR_LISTAGEM = '\033[92m'  # Verde
COR_OPERACAO = '\033[93m'  # Amarelo
COR_RELATORIO = '\033[95m' # Roxo
COR_SISTEMA = '\033[91m'   # Vermelho
RESET = '\033[0m'          # Volta para a cor padrao do terminal

# Inicializacao estruturas globais
clientes = ListaEncadeada()
produtos = ListaEncadeada()
vendas = Fila()
historico = Pilha()

# Nomes arquivos
ARQ_CLIENTES = 'clientes.txt'
ARQ_PRODUTOS = 'produtos.txt'
ARQ_VENDAS = 'vendas.txt'

# --- FUNCOES ---

def carregar_dados():
    # Carrega clientes
    if os.path.exists(ARQ_CLIENTES):
        try:
            with open(ARQ_CLIENTES, 'r') as f:
                for linha in f:
                    linha = linha.strip()
                    if linha == "": continue
                    partes = linha.split(';')
                    if len(partes) == 2:
                        clientes.inserir(Cliente(int(partes[0]), partes[1]))
        except Exception as e:
            print("Erro ao carregar clientes:", e)

    # Carrega produtos
    if os.path.exists(ARQ_PRODUTOS):
        try:
            with open(ARQ_PRODUTOS, 'r') as f:
                for linha in f:
                    linha = linha.strip()
                    if linha == "": continue
                    partes = linha.split(';')
                    if len(partes) == 4:
                        produtos.inserir(Produto(int(partes[0]), partes[1], int(partes[2]), float(partes[3])))
        except Exception as e:
            print("Erro ao carregar produtos:", e)

    # Carrega vendas
    if os.path.exists(ARQ_VENDAS):
        try:
            with open(ARQ_VENDAS, 'r') as f:
                for linha in f:
                    linha = linha.strip()
                    if linha == "": continue
                    partes = linha.split(';')
                    if len(partes) == 5:
                        vendas.enfileirar(Venda(int(partes[0]), int(partes[1]), int(partes[2]), int(partes[3]), float(partes[4])))
        except Exception as e:
            print("Erro ao carregar vendas:", e)

def salvar_dados():
    # Salva todos os clientes reescrevendo o arquivo
    try:
        with open(ARQ_CLIENTES, 'w') as f:
            for c in clientes.listar_todos():
                f.write(f"{c.id};{c.nome}\n")
    except Exception as e:
        print("Erro ao salvar clientes:", e)

    # Salva todos os produtos
    try:
        with open(ARQ_PRODUTOS, 'w') as f:
            for p in produtos.listar_todos():
                f.write(f"{p.id};{p.nome};{p.quantidade};{p.preco}\n")
    except Exception as e:
        print("Erro ao salvar produtos:", e)

    # Salva todas as vendas
    try:
        with open(ARQ_VENDAS, 'w') as f:
            for v in vendas.listar_todos():
                f.write(f"{v.id};{v.id_cliente};{v.id_produto};{v.quantidade};{v.valor_total}\n")
    except Exception as e:
        print("Erro ao salvar vendas:", e)


# --- FUNCOES AUXILIARES PARA GERAR ID ---
def gerar_id_cliente():
    lista = clientes.listar_todos()
    if len(lista) == 0: return 1
    return max([c.id for c in lista]) + 1

def gerar_id_produto():
    lista = produtos.listar_todos()
    if len(lista) == 0: return 1
    return max([p.id for p in lista]) + 1

def gerar_id_venda():
    lista = vendas.listar_todos()
    if len(lista) == 0: return 1
    return max([v.id for v in lista]) + 1


# --- FUNCAO PRINCIPAL E MENU ---
def main():
    carregar_dados()
    
    while True:
        print(f"\n{COR_SISTEMA}======================================={RESET}")
        print(f"{COR_SISTEMA}     SISTEMA DE ESTOQUE E VENDAS       {RESET}")
        print(f"{COR_SISTEMA}======================================={RESET}")
        
        print(f"\n{COR_CADASTRO}[ CADASTROS E GERENCIAMENTO ]{RESET}")
        print("1. Cadastrar cliente")
        print("2. Editar cliente")
        print("3. Cadastrar produto")
        print("4. Editar produto")
        
        print(f"\n{COR_LISTAGEM}[ CONSULTAS E LISTAGENS ]{RESET}")
        print("5. Listar clientes")
        print("6. Listar produtos do estoque")
        print("7. Pesquisar produto (nome ou id)")
        
        print(f"\n{COR_OPERACAO}[ VENDAS E OPERACOES ]{RESET}")
        print("8. Realizar venda")
        print("9. Visualizar fila de vendas")
        print("10. Desfazer ultima operacao")
        
        print(f"\n{COR_RELATORIO}[ RELATORIOS E TOTAIS ]{RESET}")
        print("11. Exibir valor total do estoque")
        print("12. Exibir valor total de vendas realizadas")
        print("13. Exibir clientes e valores totais gastos")
        
        print(f"\n{COR_SISTEMA}[ SISTEMA ]{RESET}")
        print("14. Sair")
        
        opcao_str = input("\nEscolha uma opcao: ")
        
        try:
            opcao = int(opcao_str)
        except ValueError:
            print("Erro: Digite apenas numeros validos para o menu.")
            continue

        # --- BLOCO DE CADASTROS ---
        if opcao == 1:
            nome = input("Nome do cliente: ").strip()
            if nome == "":
                print("Erro: Nome nao pode ser vazio.")
                continue
            
            novo_id = gerar_id_cliente()
            clientes.inserir(Cliente(novo_id, nome))
            historico.empilhar({"acao": "cadastro_cliente", "id": novo_id})
            salvar_dados()
            print("Cliente cadastrado com sucesso!")

        elif opcao == 2: # Editar Cliente
            id_cliente = input("Digite o ID do cliente que deseja editar: ").strip()
            
            # Mostra o nome atual antes de editar
            cliente_atual = clientes.buscar_por_id(id_cliente)
            if cliente_atual:
                print(f"Nome atual: {cliente_atual.nome}")
                novo_nome = input("Digite o novo nome (ou aperte Enter para cancelar): ").strip()
                
                if novo_nome != "":
                    # Chama o metodo que criamos na estrutura
                    clientes.editar_por_id(id_busca=id_cliente, novo_nome=novo_nome)
                    salvar_dados()
                    print("Cliente atualizado com sucesso!")
                else:
                    print("Operacao cancelada. Nome mantido.")
            else:
                print("Erro: Cliente nao encontrado.")

        elif opcao == 3:
            nome = input("Nome do produto: ").strip()
            if nome == "":
                print("Erro: Nome nao pode ser vazio.")
                continue
            
            try:
                qtd = int(input("Quantidade inicial em estoque: "))
                preco = float(input("Preco do produto: R$ "))
                if qtd < 0 or preco <= 0:
                    print("Erro: Quantidade nao pode ser negativa e preco deve ser maior que zero.")
                    continue
            except ValueError:
                print("Erro: Valores numericos invalidos.")
                continue

            novo_id = gerar_id_produto()
            produtos.inserir(Produto(novo_id, nome, qtd, preco))
            historico.empilhar({"acao": "cadastro_produto", "id": novo_id})
            salvar_dados()
            print("Produto cadastrado com sucesso!")

        elif opcao == 4: # Editar Produto
            id_produto = input("Digite o ID do produto que deseja editar: ").strip()
            
            # Mostra os dados atuais
            produto_atual = produtos.buscar_por_id(id_produto)
            if produto_atual:
                print(f"Dados atuais -> Nome: {produto_atual.nome} | Preco: R$ {produto_atual.preco:.2f}")
                
                novo_nome = input("Novo nome (ou Enter para manter o atual): ").strip()
                novo_preco_str = input("Novo preco (ou Enter para manter o atual): ").strip()
                
                # Trata o preco digitado
                novo_preco = None
                if novo_preco_str != "":
                    try:
                        novo_preco = float(novo_preco_str)
                    except ValueError:
                        print("Erro: O preco digitado nao e valido. O preco antigo sera mantido.")

        # --- BLOCO DE LISTAGENS ---
        elif opcao == 5:
            lista = clientes.listar_todos()
            if len(lista) == 0: print("Nenhum cliente cadastrado.")
            else:
                print("\nLista de Clientes:")
                for c in lista: print(f"ID: {c.id} | Nome: {c.nome}")

        elif opcao == 6:
            lista = produtos.listar_todos()
            if len(lista) == 0: print("Nenhum produto em estoque.")
            else:
                print("\nEstoque atual:")
                for p in lista: print(f"ID: {p.id} | Nome: {p.nome} | Qtd: {p.quantidade} | Preco: R$ {p.preco:.2f}")

        elif opcao == 7:
            termo = input("Digite o ID ou o Nome do produto: ").strip()
            if termo == "": continue

            produto_encontrado = produtos.buscar_por_id(termo)
            if produto_encontrado:
                print(f"Produto Encontrado -> ID: {produto_encontrado.id} | Nome: {produto_encontrado.nome} | Qtd: {produto_encontrado.quantidade}")
            else:
                resultados = produtos.buscar_por_nome(termo)
                if len(resultados) == 0: print("Nenhum produto encontrado.")
                else:
                    for p in resultados: print(f"ID: {p.id} | Nome: {p.nome} | Qtd: {p.quantidade}")

        # --- BLOCO DE OPERACOES ---
        elif opcao == 8:
            try:
                id_cliente = int(input("ID do cliente: "))
                id_produto = int(input("ID do produto: "))
                qtd_venda = int(input("Quantidade a vender: "))
            except ValueError:
                print("Erro: Entradas devem ser numeros inteiros.")
                continue

            cliente = clientes.buscar_por_id(id_cliente)
            produto = produtos.buscar_por_id(id_produto)

            if cliente is None: print("Erro: Cliente nao encontrado."); continue
            if produto is None: print("Erro: Produto nao encontrado."); continue
            if qtd_venda <= 0: print("Erro: Quantidade de venda invalida."); continue
            if produto.quantidade < qtd_venda: print(f"Erro: Estoque insuficiente ({produto.quantidade} disp.)."); continue

            valor_total = qtd_venda * produto.preco
            produto.quantidade -= qtd_venda 
            
            nova_venda_id = gerar_id_venda()
            vendas.enfileirar(Venda(nova_venda_id, id_cliente, id_produto, qtd_venda, valor_total))
            historico.empilhar({"acao": "venda", "id_produto": id_produto, "quantidade_vendida": qtd_venda})
            salvar_dados()
            print(f"Venda realizada! Valor Total: R$ {valor_total:.2f}")

        elif opcao == 9:
            lista = vendas.listar_todos()
            if len(lista) == 0: print("Nenhuma venda realizada.")
            else:
                for v in lista: print(f"ID: {v.id} | Cliente: {v.id_cliente} | Prod: {v.id_produto} | Qtd: {v.quantidade} | Total: R$ {v.valor_total:.2f}")

        elif opcao == 10:
            ultima_acao = historico.desempilhar()
            if ultima_acao is None:
                print("Erro: Nao ha operacoes para desfazer.")
                continue

            tipo = ultima_acao["acao"]
            if tipo == "cadastro_cliente":
                clientes.remover_por_id(ultima_acao["id"])
                print("Cadastro de cliente desfeito.")
            elif tipo == "cadastro_produto":
                produtos.remover_por_id(ultima_acao["id"])
                print("Cadastro de produto desfeito.")
            elif tipo == "venda":
                prod = produtos.buscar_por_id(ultima_acao["id_produto"])
                if prod: prod.quantidade += ultima_acao["quantidade_vendida"]
                vendas.remover_ultimo()
                print("Venda desfeita e estoque restaurado.")
            salvar_dados()

        # --- BLOCO DE RELATORIOS ---
        elif opcao == 11:
            lista = produtos.listar_todos()
            total = sum([(p.quantidade * p.preco) for p in lista])
            print(f"Valor total do estoque: R$ {total:.2f}")

        elif opcao == 12:
            lista = vendas.listar_todos()
            total = sum([v.valor_total for v in lista])
            print(f"Valor total de vendas: R$ {total:.2f}")

        elif opcao == 13:
            lista_clientes = clientes.listar_todos()
            lista_vendas = vendas.listar_todos()
            for c in lista_clientes:
                gasto = sum([v.valor_total for v in lista_vendas if v.id_cliente == c.id])
                print(f"Cliente: {c.nome} | Total Gasto: R$ {gasto:.2f}")

        # --- SAIDA ---
        elif opcao == 14:
            print("Encerrando o sistema...")
            break
            
        else:
            print("Erro: Opcao invalida.")

# Verifica se o arquivo atual e o principal para iniciar
if __name__ == "__main__":
    main()