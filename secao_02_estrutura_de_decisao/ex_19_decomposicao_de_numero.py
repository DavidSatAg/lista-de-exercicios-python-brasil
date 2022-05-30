"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = ((numero % 100) % 10)
    casas = 0
    centenas_str = dezenas_str = unidades_str = ''
    if numero < 0:
        print("'O número precisa ser positivo'")
    if numero > 999:
        print("'O número precisa ser menor que 1000'")
    else:
        if centenas == 1:
            centenas_str = 'centena'
            casas += 1
        elif centenas > 1:
            centenas_str = 'centenas'
            casas += 1
        if dezenas == 1:
            dezenas_str = 'dezena'
            casas += 1
        elif dezenas > 1:
            dezenas_str = 'dezenas'
            casas += 1
        if unidades == 1:
            unidades_str = 'unidade'
            casas += 1
        elif unidades > 1:
            unidades_str = 'unidades'
            casas += 1
        if casas == 1:
            if centenas != 0:
                print(f"'{numero} = {centenas} {centenas_str}'")
            elif dezenas != 0:
                print(f"'{numero} = {dezenas} {dezenas_str}'")
            else:
                print(f"'{numero} = {unidades} {unidades_str}'")
        elif casas == 3:
            print(f"'{numero} = {centenas} {centenas_str}, {dezenas} {dezenas_str} e {unidades} {unidades_str}'")
        elif casas == 2:
            if centenas == 0:
                print(f"'{numero} = {dezenas} {dezenas_str} e {unidades} {unidades_str}'")
            elif dezenas == 0:
                print(f"'{numero} = {centenas} {centenas_str} e {unidades} {unidades_str}'")
            elif unidades == 0:
                print(f"'{numero} = {centenas} {centenas_str} e {dezenas} {dezenas_str}'")



