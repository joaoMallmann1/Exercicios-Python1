"""
Faça um programa que leia o valor da hora trabalhada (em reais) e número de horas trabalhadas no mês. Imprima o
valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""
valor_hora = float(input('Digite o valor da hora trabalhada: '))
numero_horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

print(f'O valor a ser pago ao funcionário é de {(valor_hora * numero_horas) + ((valor_hora * numero_horas) * 0.10):.2f}'
      )
