"""
    UNIVERSIDADE FEDERAL DE SANTA CATARINA
    INE5429 - Seguranca em Computacao
    Professor Ricardo Felipe Custodio
    Graduando Rodrigo Pedro Marques
    Matricula 12200660
"""

from euler import totient

"""
    Funcao para achar os fatores primos de n.
    Retorna os fatores primos que compoe n
"""
def fatores_primos(n):
    fatores = []        #Lista dos fatores primos

    i = 2               #Inicia em 2 pois nao pode ser 0 ou 1.
    while i**2 <= n:
        if n % i == 0:
            n = n // i
            fatores.append(i)
        i += 1

    fatores.append(n)
    return fatores

"""
    Funcao para achar as raizes primitivas de n.
    Retorna uma lista de raizes primitivas de n.
"""
def calcula_raizes_primitivas(n):
    totiente_de_euler = len(totient(n)) #Valor do totiente
    fatores = fatores_primos(totiente_de_euler) #Lista de fatores primos que compoem o totiente.
    numero_raizes_primitivas = len(totient(totiente_de_euler)) # Numero de raizes primitivas
    raizes_primitivas = []  #Lista de raizes primitivas

    i = 1
    while len(raizes_primitivas) != numero_raizes_primitivas:
        a = i   #Numero a ser testado
        if all(((a**(totiente_de_euler//factor)) % n) != 1 for factor in fatores): #Se para todo 'a' elevado ao totiente, dividido pelos fatores primos, modulo n for diferente de 1 entao e uma raiz primitiva.  
            raizes_primitivas.append(a)
        i += 1

    return raizes_primitivas

