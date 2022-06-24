"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    import math
    area_a_ser_pintada = float(input("Insira a área em metros quadrados a ser pintada: "))
    tinta_necessaria = math.ceil((area_a_ser_pintada / 6) * 1.1)
    latas_necessarias = math.ceil(tinta_necessaria / 18)
    preco_latas = latas_necessarias * 80
    galoes_necessarios = math.ceil(tinta_necessaria / 3.6)
    preco_galoes = galoes_necessarios * 25
    tinta_restante_latas = (latas_necessarias * 18) - tinta_necessaria
    tinta_restante_galoes = (galoes_necessarios * 3.6) - tinta_necessaria
    latas_necessarias_economico = tinta_necessaria // 18
    galoes_necessarios_economico = math.ceil((tinta_necessaria % 18) / 3.6)
    preco_economico = (latas_necessarias_economico * 80) + (galoes_necessarios_economico * 25)
    restante_economico = (latas_necessarias_economico * 18) + (galoes_necessarios_economico * 3.6) - tinta_necessaria
    print(f"Você deve comprar {tinta_necessaria:.0f} litros de tinta.")
    print(f"Você pode comprar {latas_necessarias} lata(s) de 18 litros a um custo de R$ {preco_latas:.0f}. Vão sobrar {tinta_restante_latas:.1f} litro(s) de tinta.")
    print(f"Você pode comprar {galoes_necessarios:} lata(s) de 3.6 litros a um custo de R$ {preco_galoes:.0f}. Vão sobrar {tinta_restante_galoes:.1f} litro(s) de tinta.")
    print(f"Para menor custo, você pode comprar {latas_necessarias_economico:.0f} lata(s) de 18 litros e {galoes_necessarios_economico} galão(ões) de 3.6 litros a um custo de R$ {preco_economico:.0f}. Vão sobrar {restante_economico:.1f} litro(s) de tinta.")

