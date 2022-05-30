"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    if "/" not in data:
        print("'Data inválida'")
    else:    
        dia, mes, ano = data.split("/")
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        if mes > 12 or mes < 1:
            print("'Data inválida'")
        else:
            if mes == 2:
                if dia > 29 or dia < 1:
                    print("'Data inválida'")
                else: print("'Data válida'")

        
    


