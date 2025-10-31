""" Crie um programa para ordenar um conjunto de strings pelo seu tamanho. Seu programa deve receber um conjunto de strings e retornar este mesmo conjunto ordenado pelo tamanho das palavras, se o tamanho das strings for igual, deve-se manter a ordem original do conjunto."""

"""Entrada
A primeira linha da entrada possui um único inteiro N, que indica o número de casos de teste. Cada caso de teste poderá conter de 1 a 50 strings inclusive, e cada uma das strings poderá conter entre 1 e 50 caracteres inclusive. Os caracteres poderão ser espaços, letras, ou números."""

numero_casos = int(input())

for x in range(numero_casos):
    lista = input()
    lista = lista.split()
    for i in range(len(lista)):
        for j in range(len(lista) -1, i, -1):
            if len(lista[j]) > len(lista[j - 1]):
                lista[j], lista[j - 1] = lista[j - 1], lista[j]
    for i in range(len(lista)):
        if i < len(lista) -1:
            print(lista[i], end=" ")
        else:
            print(lista[i])