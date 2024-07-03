"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento
de 25%
"""
salario = float(input("Digite o salário do funcionário: "))

print(f'O salário com o reajuste será de R${salario + (salario * 0.25):.2f}')
