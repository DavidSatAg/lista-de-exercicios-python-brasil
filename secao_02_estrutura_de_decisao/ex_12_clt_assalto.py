"""
Exercício 12 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
  Salário Bruto até 900 (inclusive) - isento
  Salário Bruto até 1500 (inclusive) - desconto de 5%
  Salário Bruto até 2500 (inclusive) - desconto de 10%
  Salário Bruto acima de 2500 - desconto de 20%

Mostrar valores monetários com duas casas decimais, alinhados à direita, com espaço para 5 dígitos de salário, ou seja,
até R$ 99999,99

    >>> calcular_salario_liquido(1, 160)
    Salário Bruto: (R$ 1.00 * 160)     : R$   160.00
    (-) IR (0%)                        : R$     0.00
    (-) INSS (10%)                     : R$    16.00
    (-) Sindicato (3%)                 : R$     4.80
    FGTS (11%)                         : R$    17.60
    Total de descontos                 : R$    20.80
    Salário Liquido                    : R$   139.20
    >>> calcular_salario_liquido(5, 220)
    Salário Bruto: (R$ 5.00 * 220)     : R$  1100.00
    (-) IR (5%)                        : R$    55.00
    (-) INSS (10%)                     : R$   110.00
    (-) Sindicato (3%)                 : R$    33.00
    FGTS (11%)                         : R$   121.00
    Total de descontos                 : R$   198.00
    Salário Liquido                    : R$   902.00
    >>> calcular_salario_liquido(10, 160)
    Salário Bruto: (R$ 10.00 * 160)    : R$  1600.00
    (-) IR (10%)                       : R$   160.00
    (-) INSS (10%)                     : R$   160.00
    (-) Sindicato (3%)                 : R$    48.00
    FGTS (11%)                         : R$   176.00
    Total de descontos                 : R$   368.00
    Salário Liquido                    : R$  1232.00
    >>> calcular_salario_liquido(100, 160)
    Salário Bruto: (R$ 100.00 * 160)   : R$ 16000.00
    (-) IR (20%)                       : R$  3200.00
    (-) INSS (10%)                     : R$  1600.00
    (-) Sindicato (3%)                 : R$   480.00
    FGTS (11%)                         : R$  1760.00
    Total de descontos                 : R$  5280.00
    Salário Liquido                    : R$ 10720.00

"""


def calcular_salario_liquido(valor_hora: float, horas_trabalhadas: int):
    """Escreva aqui em baixo a sua solução"""
    calcular_salario_liquido = (valor_hora, horas_trabalhadas) 
    salario_bruto = valor_hora * horas_trabalhadas
    if salario_bruto <= 900:
        ir = 0
    elif salario_bruto > 900 and salario_bruto <= 1500:
        ir = 5
    elif salario_bruto > 1500 and salario_bruto <= 2500:
        ir = 10
    elif salario_bruto > 2500:
        ir = 20
    inss = 10
    sindicato = 3
    fgts = 11
    desconto_ir = float(((salario_bruto * ir) / 100))
    desconto_inss = float(((salario_bruto * inss) / 100))
    desconto_sindicato = float((salario_bruto * sindicato) / 100)
    desconto_fgts = float((salario_bruto * fgts) / 100)
    total_desconto = float(salario_bruto * (ir + inss + sindicato) / 100)
    salario_liquido = salario_bruto - total_desconto
    linha_1 = f"Salário Bruto: (R$ {valor_hora:.2f} * {horas_trabalhadas})"
    linha_2 = f"(-) IR ({ir}%)"
    linha_3 = f"(-) INSS ({inss}%)"
    linha_4 = f"(-) Sindicato ({sindicato}%)"
    linha_5 = f"FGTS ({fgts}%)"
    linha_1num = f"{salario_bruto:.2f}"
    linha_2num = f"{desconto_ir:.2f}"
    linha_3num = f"{desconto_inss:.2f}"
    linha_4num = f"{desconto_sindicato:.2f}"
    linha_5num = f"{desconto_fgts:.2f}"
    linha_6num = f"{total_desconto:.2f}"
    linha_7num = f"{salario_liquido:.2f}"
    print(linha_1.ljust(34), ": R$", linha_1num.rjust(8))
    print(linha_2.ljust(34), ": R$", linha_2num.rjust(8))
    print(linha_3.ljust(34), ": R$", linha_3num.rjust(8))
    print(linha_4.ljust(34), ": R$", linha_4num.rjust(8))
    print(linha_5.ljust(34), ": R$", linha_5num.rjust(8))
    print(f"Total de descontos                 : R$", linha_6num.rjust(8))
    print(f"Salário Liquido                    : R$", linha_7num.rjust(8))





