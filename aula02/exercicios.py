"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def remove_negativos(lista):
    """Devolve uma lista nova so com os numeros que nao sao negativos."""
    resultado = []
    for numero in lista:
        if numero >= 0:
            resultado.append(numero)
    return resultado


def inverte(lista):
    """Devolve uma lista nova na ordem contraria.
    Sem usar reverse() e sem usar [::-1]."""
    resultado = []
    for i in range(len(lista) - 1, -1, -1):
        resultado.append(lista[i])
    return resultado


def busca_binaria(lista, alvo):
    """Recebe uma lista JA ORDENADA. Devolve a posicao do alvo, ou -1."""
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def intercala(lista_a, lista_b):
    """Devolve uma lista nova alternando os elementos das duas.
    As duas listas tem o mesmo tamanho."""
    resultado = []
    for i in range(len(lista_a)):
        resultado.append(lista_a[i])
        resultado.append(lista_b[i])
    return resultado


def remove_repetidos(lista):
    """(Desafio) Devolve uma lista nova sem repetidos,
    mantendo a ordem da primeira aparicao."""
    resultado = []
    vistos = set()
    for elemento in lista:
        if elemento not in vistos:
            resultado.append(elemento)
            vistos.add(elemento)
    return resultado
