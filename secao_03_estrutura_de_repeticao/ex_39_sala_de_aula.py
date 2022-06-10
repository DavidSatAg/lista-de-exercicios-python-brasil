"""
Exercício 39 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o nome do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o nome do aluno mais alto
 e o número do aluno mais baixo, junto com suas alturas.
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162))
    'O maior aluno é o Renzo com 162 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165))
    'O maior aluno é o Clara com 165 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165), ('Oscar', 199))
    'O maior aluno é o Oscar com 199 cm. O menor aluno é o Renzo com 162 cm'

"""


def calcular_aluno_mais_baixo_e_mais_alto(*alunos) -> str:
    """Escreva aqui em baixo a sua solução"""
    lista_alunos = []
    for nome, altura in alunos:
        lista_alunos.append([nome,altura])
    mais_alto = mais_baixo = int(lista_alunos[0][1])
    nome_mais_alto = nome_mais_baixo = lista_alunos[0][0]
    i = 0
    for i in range(len(lista_alunos)):
        if int(lista_alunos[i][1]) > mais_alto:
            mais_alto = int(lista_alunos[i][1])
            nome_mais_alto = lista_alunos[i][0]
        if int(lista_alunos[i][1]) < mais_baixo:
            mais_baixo = int(lista_alunos[i][1])
            nome_mais_baixo = lista_alunos[i][0]
    print(f"'O maior aluno é o {nome_mais_alto} com {mais_alto} cm. O menor aluno é o {nome_mais_baixo} com {mais_baixo} cm'")
