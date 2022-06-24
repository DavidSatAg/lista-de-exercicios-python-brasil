"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Tamanho de strings. Faça um programa que compare 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings


    >>> comparar('Brasil Hexa 2006', 'Brasil! Hexa 2006!')
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.
    >>> comparar('Igual', 'Igual')
    String 1: Igual
    String 2: Igual
    Tamanho de "Igual": 5 caracteres
    Tamanho de "Igual": 5 caracteres
    As duas strings possuem  mesmo tamanho.
    As duas strings possuem conteúdo igual.

"""


def comparar(s1: str, s2: str):
    """Escreva aqui em baixo a sua solução"""
    tamanho_igual = False
    string_igual = False
    if len(s1) == len(s2):
        tamanho_igual = True
        if s1 == s2:
            string_igual = True
    imprimir_resultado(s1, s2, tamanho_igual, string_igual)


def imprimir_resultado(s1, s2, valor1, valor2):
    print(f"String 1: {s1}")
    print(f"String 2: {s2}")
    print(f'Tamanho de "{s1}": {len(s1)} caracteres')
    print(f'Tamanho de "{s2}": {len(s2)} caracteres')
    if valor1:
        print("As duas strings possuem  mesmo tamanho.")
    else:
        print("As duas strings são de tamanhos diferentes.")
    if valor2:
        print("As duas strings possuem conteúdo igual.")
    else:
        print("As duas strings possuem conteúdo diferente.")

