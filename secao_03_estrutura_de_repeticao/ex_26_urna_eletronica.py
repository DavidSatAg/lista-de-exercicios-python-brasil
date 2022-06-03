"""
Exercício 26 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

uma eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar
 e ao final mostrar o número de votos de cada candidato.

    >>> calcular_votos()
    Votantes: 0
    Votos no candidato corrupto: 0
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto')
    Votantes: 1
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso')
    Votantes: 2
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 3
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 1
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz', 'corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 6
    Votos no candidato corrupto: 2
    Votos no candidato mentiroso: 2
    Votos no candidato rouba, mas faz: 2

"""


def calcular_votos(*votos):
    """Escreva aqui em baixo a sua solução"""
    votantes = len(votos)
    votos_corrupto = 0
    votos_mentiroso = 0
    votos_rouba_mas_faz = 0 
    for i in votos:
        if i == 'corrupto':
            votos_corrupto += 1
        elif i == 'mentiroso':
            votos_mentiroso += 1
        elif i == 'rouba, mas faz':
            votos_rouba_mas_faz += 1
    print(f"Votantes: {votantes}")
    print(f"Votos no candidato corrupto: {votos_corrupto}")
    print(f"Votos no candidato mentiroso: {votos_mentiroso}")
    print(f"Votos no candidato rouba, mas faz: {votos_rouba_mas_faz}")
        
