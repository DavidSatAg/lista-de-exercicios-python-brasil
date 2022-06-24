"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    maior_indice_acidentes = menor_indice_acidentes = (int(cidades[0][2]) * 1000) / int(cidades[0][1])
    nome_cidade_maior_indice = nome_cidade_menor_indice = cidades[0][0]
    i = 0
    total_veiculos = 0
    contador = 0
    acidentes_cidade_menos_150_000_habitantes = 0
    for i in range(len(cidades)):
        indice_de_acidentes = (int(cidades[i][2]) * 1000) / int(cidades[i][1])
        if indice_de_acidentes > maior_indice_acidentes:
            maior_indice_acidentes = indice_de_acidentes
            nome_cidade_maior_indice = cidades[i][0]
        if indice_de_acidentes < menor_indice_acidentes:
            menor_indice_acidentes = indice_de_acidentes
            nome_cidade_menor_indice = cidades[i][0]
        if int(cidades[i][1] <= 150_000):
            contador += 1
            acidentes_cidade_menos_150_000_habitantes += int(cidades[i][2])
        total_veiculos += int(cidades[i][1])
    media = total_veiculos / len(cidades)
    media_de_acidentes_total_cidade_menos_150_000_habitantes = acidentes_cidade_menos_150_000_habitantes / contador
    print(f"O maior índice de acidentes é de {nome_cidade_maior_indice}, com {maior_indice_acidentes:.1f} acidentes por mil carros.")
    print(f"O menor índice de acidentes é de {nome_cidade_menor_indice}, com {menor_indice_acidentes:.1f} acidentes por mil carros.")
    print(f"O média de veículos por cidade é de {media:.0f}.")
    print(f"A média de acidentes total nas cidades com menos de 150 mil carros é de {media_de_acidentes_total_cidade_menos_150_000_habitantes:.1f} acidentes.")
        
