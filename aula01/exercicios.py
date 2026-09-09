"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    """Devolve a soma de todos os numeros da lista. Lista vazia devolve 0."""
    total = 0
    for numero in lista:
        total += numero
    return total


def conta_pares(lista):
    """Devolve quantos numeros da lista sao pares."""
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
         contador += 1
    return contador


def maior_valor(lista):
    """Devolve o maior numero da lista. A lista nao esta vazia."""
    maior = lista[0]
    for numero in lista:
        if numero > maior:
         maior = numero
    return maior


def existe(lista, alvo):
    """Devolve True se o alvo esta na lista, False se nao esta."""
    return alvo in lista


def busca_linear(lista, alvo):
    """Devolve a posicao do alvo na lista, ou -1 se ele nao estiver."""
    for indice, numero in enumerate(lista):
        if numero == alvo:
            return indice
    return -1


def segundo_maior(lista):
    """(Desafio) Devolve o segundo maior, percorrendo a lista uma unica vez."""
    if len(lista) < 2:
        return None

    maior = segundo = float('-inf')
    for numero in lista:
        if numero > maior:
            segundo = maior
            maior = numero
        elif numero > segundo:
            segundo = numero

    return segundo if segundo != float('-inf') else None
