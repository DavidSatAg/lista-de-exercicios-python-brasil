"""
Exercício 24 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o mostre a média aritmética de N notas.

    >>> calcular_media()
    'É necessária ao menos uma nota para calcular a média'
    >>> calcular_media(1)
    1
    >>> calcular_media(1, 3)
    2
    >>> calcular_media(1, 3, 3)
    2.3333333333333335

"""


def calcular_media(*notas) -> float:
    """Escreva aqui em baixo a sua solução"""
    if len(notas) > 0:
        soma = 0
        i = 0
        while i < len(notas):
            soma += notas[i]
            i += 1
        media = soma / len(notas)
        inteiro, decimal = str(media).split(".")
        if round(int(decimal)) == 0:
            print(inteiro)
        else:
            print(media)
    else:
        print("'É necessária ao menos uma nota para calcular a média'")

