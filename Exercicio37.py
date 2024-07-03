"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto
"""
valor = float(input('Digite o valor do produto: '))
desconto = float(input('Digite a porcentagem do desconto: '))

valor_desconto = valor * (desconto / 100)
valorComDesconto = valor - valor_desconto

print(f'O valor original do produto era de R${valor:.2f}')
print(f'O valor do desconto é de R${valor_desconto:.2f}')
print(f'O valor após o desconto ficou como R${valorComDesconto:.2f}')
