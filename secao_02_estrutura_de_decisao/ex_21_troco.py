"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    notas_100, valor = divmod(valor, 100)
    notas_50, valor = divmod(valor, 50)
    notas_10, valor = divmod(valor, 10)
    notas_5, notas_1 = divmod(valor, 5)
    contador = 0
    str_100 = str_50 = str_10 = str_5 = str_1 = ''
    if notas_1 == 1:
        str_1 = '1 nota de R$ 1'
        contador += 1
    elif notas_1 > 1:
        str_1 = f'{notas_1} notas de R$ 1'
        contador += 1
    if notas_5 == 1:
        str_5 = '1 nota de R$ 5'
        contador += 1
    elif notas_5 > 1:
        str_5 = f'{notas_5} notas de R$ 5'
        contador += 1
    if notas_10 == 1:
        str_10 = '1 nota de R$ 10'
        contador += 1
    elif notas_10 > 1:
        str_10 = f'{notas_10} notas de R$ 10'
        contador += 1
    if notas_50 == 1:
        str_50 = '1 nota de R$ 50'
        contador += 1
    elif notas_50 > 1:
        str_50 = f'{notas_50} notas de R$ 50'
        contador += 1
    if notas_100 == 1:
        str_100 = '1 nota de R$ 100'
        contador += 1
    elif notas_100 > 1:
        str_100 = f'{notas_100} notas de R$ 100'
        contador += 1
    if contador == 1:
        print(f"'{str_100}{str_50}{str_10}{str_5}{str_1}'")
    if contador == 2:
        print(f"'{str_10} e {str_1}'")
    if contador == 4:
        print(f"'{str_100}, {str_50}, {str_5} e {str_1}'")
    if contador == 5:
        print(f"'{str_100}, {str_50}, {str_10}, {str_5} e {str_1}'")
    

        
