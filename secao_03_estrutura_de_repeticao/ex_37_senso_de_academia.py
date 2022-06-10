"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


from http.client import NON_AUTHORITATIVE_INFORMATION


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    lista_clientes = []
    while True:
        nome = input("Digite o nome: ")
        if nome == "0":
            break
        altura = input("Digite a altura: ")
        peso = input("Digite o peso: ")
        clientes = [nome, altura, peso]
        lista_clientes.append(clientes)
    i = 0
    total_altura = total_peso = 0
    mais_alto = mais_baixo = int(lista_clientes[0][1])
    nome_mais_alto = nome_mais_baixo = lista_clientes[0][0]
    mais_pesado = mais_leve = int(lista_clientes[0][2])
    nome_mais_pesado = nome_mais_leve = lista_clientes[0][0]
    for i in range(len(lista_clientes)):
        if int(lista_clientes[i][1]) > mais_alto:
            mais_alto = int(lista_clientes[i][1])
            nome_mais_alto = lista_clientes[i][0]
        if int(lista_clientes[i][1]) < mais_baixo:
            mais_baixo = int(lista_clientes[i][1])
            nome_mais_baixo = lista_clientes[i][0]
        if int(lista_clientes[i][2]) > mais_pesado:
            mais_pesado = int(lista_clientes[i][2])
            nome_mais_pesado = lista_clientes[i][0]
        if int(lista_clientes[i][2]) < mais_leve:
            mais_leve = int(lista_clientes[i][2])
            nome_mais_leve = lista_clientes[i][0]
        total_altura += int(lista_clientes[i][1])
        total_peso += int(lista_clientes[i][2])
    media_altura = total_altura / len(lista_clientes)
    media_peso = total_peso / len(lista_clientes)
    print(f"Cliente mais alto: {nome_mais_alto}, com {mais_alto} centímetros")
    print(f"Cliente mais baixo: {nome_mais_baixo}, com {mais_baixo} centímetros")
    print(f"Cliente mais magro: {nome_mais_leve}, com {mais_leve} kilos")
    print(f"Cliente mais gordo: {nome_mais_pesado}, com {mais_pesado} kilos")
    print("--------------------------------------------------")
    print(f"Media de altura dos clientes: {media_altura:.1f} centímetros")
    print(f"Media de peso dos clientes: {media_peso:.1f} kilos")

