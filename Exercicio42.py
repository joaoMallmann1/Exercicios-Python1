"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo que esse funcionário tem
uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.
"""
salario_base = float(input('Digite o salário-base do funcionário: '))

gratificacao = salario_base * 0.05

imposto = salario_base * 0.07

salario_a_receber = salario_base + gratificacao - imposto

print(f'O salário a receber é de R${salario_a_receber:.2f}')
