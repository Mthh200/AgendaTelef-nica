# -*- coding: utf-8 -*-
"""
AGENDA TELEFÔNICA - Esqueleto do Trabalho Final
Disciplina: Fundamentos de Programação
Prazo de entrega: 30/06/2026

COMO OS DADOS SÃO ORGANIZADOS
-----------------------------
Cada CONTATO é representado por um DICIONÁRIO, por exemplo:

    {"nome": "Ana Souza", "telefone": "(11) 91234-5678", "email": "ana@email.com"}

Todos os contatos ficam guardados em uma LISTA de dicionários.

SUA TAREFA
----------
- A função cadastrar_contato() já vem PRONTA, como modelo.
- Implemente o corpo das demais funções marcadas com "# TODO".
- O menu, o laço principal e as mensagens já estão prontos como referência.

Para executar no terminal:
    python agenda_telefonica.py
"""


# =====================================================================
# FUNÇÕES DO SISTEMA
# =====================================================================

def exibir_menu():
    """Mostra as opções disponíveis na tela."""
    print("\n===== AGENDA TELEFÔNICA =====")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Editar contato")
    print("5 - Remover contato")
    print("0 - Sair")
    print("=============================")


def cadastrar_contato(contatos):
    # Lê os dados de um novo contato e adiciona à lista.

    print("\n--- Novo contato ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
    }

    contatos.append(contato)
    print(f"Contato '{nome}' cadastrado com sucesso!")
    print("\n--------------------")


def listar_contatos(contatos):
    # Mostra todos os contatos cadastrados.

    print("--- Lista de contatos ---")
    if len(contatos) > 0:
        for contato in contatos:
            print(f"Nome: {contato.nome}")
            print(f"Telefone: {contato.telefone}")
            print(f"Email: {contato.email}")
            print("--------------------")
    else:
        print("\nNenhum contato cadastrado ainda")
        print("\n--------------------")


def buscar_contato(contatos):
    """Procura contatos pelo nome (ou parte do nome).

    Passos sugeridos:
      1. Peça o texto a procurar com input().
      2. Percorra a lista comparando com o campo "nome" de cada contato.
      3. Mostre os que combinarem; se nenhum combinar, avise o usuário.
    """
    # TODO: implementar
    nome = input("Buscar contato pelo nome: ")
    
    print(f'--- Buscando por {nome}"" ---')

    count = 0
    for contato in contatos:
        if nome in contato.nome:
            print(f"Nome: {contato.nome}")
            print(f"Telefone: {contato.telefone}")
            print(f"Email: {contato.email}")
            print("--------------------")
            count += 1
    if count == 0:
        print("Nenhum contato corresponde à busca")
        print("\n--------------------")

def editar_contato(contatos):
    """Altera os dados de um contato já cadastrado.

    Passos sugeridos:
      1. Peça o nome do contato a editar e localize-o na lista.
      2. Se encontrar, peça os novos dados e atualize as chaves do dicionário.
      3. Se não encontrar, avise o usuário.
    """
    # TODO: implementar
    edit = input("Qual o nome do contato que deseja editar? ")
    buscar_contato(contatos)

    print(">> [função ainda não implementada]")

def remover_contato(contatos):
    """Remove um contato da lista.

    Passos sugeridos:
      1. Peça o nome do contato a remover e localize-o na lista.
      2. Se encontrar, use contatos.remove(...) e confirme a remoção.
      3. Se não encontrar, avise o usuário.
    """
    # TODO: implementar
    print(">> [função ainda não implementada]")


# =====================================================================
# PROGRAMA PRINCIPAL
# =====================================================================

def main():
    contatos = []  # lista que guarda todos os contatos (dicionários)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_contato(contatos)
        elif opcao == "2":
            listar_contatos(contatos)
        elif opcao == "3":
            buscar_contato(contatos)
        elif opcao == "4":
            editar_contato(contatos)
        elif opcao == "5":
            remover_contato(contatos)
        elif opcao == "0":
            print("\nEncerrando a agenda. Até logo!")
            break
        else:
            print("Opção inválida! Digite um número de 0 a 5.")


# Ponto de partida do programa
main()
