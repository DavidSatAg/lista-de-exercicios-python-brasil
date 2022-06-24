"""
Exercício 09 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que receba um vestor de números inteiros, calcule e mostre a soma dos quadrados dos elementos do
vetor.

    >>> calcular_soma_de_quadrados([])
    0
    >>> calcular_soma_de_quadrados([1])
    1
    >>> calcular_soma_de_quadrados([1, 2])
    5
    >>> calcular_soma_de_quadrados(list(range(10)))
    285

"""


def calcular_soma_de_quadrados(inteiros: list) -> int:
    """Escreva aqui em baixo a sua solução"""
    # if inteiros == []:
    #     print("0")
    # else:
    #     n = inteiros[-1]
    #     print(f"{(n * (2 * n + 1) * (n + 1)) / 6:.0f}")

    soma_de_quadrados = 0
    for numero in inteiros:
        soma_de_quadrados += numero ** 2
    print(soma_de_quadrados)