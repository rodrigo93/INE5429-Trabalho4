"""
    UNIVERSIDADE FEDERAL DE SANTA CATARINA
    INE5429 - Seguranca em Computacao
    Professor Ricardo Felipe Custodio
    Graduando Rodrigo Pedro Marques
    Matricula 12200660
"""

from fractions import gcd   #Importa a funcao de de maior divisor comum

"""
    Funcao que calcula o totiente de Euler e seus coprimos.
    O tamanho da lista e o totiente de Euler.
"""
def totient(n):
    primos_relativos = []   #Lista de primos relativos
    for i in range(n):
        if gcd(i, n) == 1:
            primos_relativos.append(i)  #Caso o maior divisor comum entre os numeros for 1, adiciona na lista.
    return primos_relativos

