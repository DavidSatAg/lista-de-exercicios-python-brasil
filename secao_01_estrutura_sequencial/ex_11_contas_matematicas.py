"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 1) o produto do dobro do primeiro com metade do segundo;
 2) a soma do triplo do primeiro com o terceiro;
 3) o terceiro elevado ao cubo.

 Apresente os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_11_contas_matematicas
    >>> numeros = ['3.14', '43', '42']
    >>> ex_11_contas_matematicas.input = lambda k: numeros.pop()
    >>> ex_11_contas_matematicas.calcular_formulas()
    O produto do dobro do primeiro com metade do segundo é 1806.00
    A soma do triplo do primeiro com o terceiro é 129.14
    O terceiro elevado ao cubo é 30.96

"""


def calcular_formulas():
    """Escreva aqui em baixo a sua solução"""
    num_1_inteiro = int(input("Digite o primeiro número inteiro: "))
    num_2_inteiro = int(input("Digite o segundo número inteiro: "))
    num_1_real = float(input("Digite o primeiro número real: "))
    operacao_1 = (2 * num_1_inteiro) * (num_2_inteiro / 2)
    operacao_2 = (3 * num_1_inteiro) + num_1_real
    operacao_3 = num_1_real ** 3
    print(f"O produto do dobro do primeiro com metade do segundo é {operacao_1:.2f}")
    print(f"A soma do triplo do primeiro com o terceiro é {operacao_2:.2f}")
    print(f"O terceiro elevado ao cubo é {operacao_3:.2f}")

