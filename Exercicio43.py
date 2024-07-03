"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

- o total a pagar com desconto de 10%
- o valor de cada parcela, no parcelamento de 3X sem juros
- a comissão do vendedor, no caso de vender a vista (5% sobre o valor com desconto)
- a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""
valor = float(input('Digite o valor do produto: '))

total_desconto = valor - (valor * 0.10)

parcela = valor / 3

comissao1 = (total_desconto * 0.05)

comissao2 = valor * 0.05

print(f'O total a pagar com desconto de 10%: R${total_desconto:.2f}')
print(f'O valor de cada parcela (3X sem juros): R${parcela:.2f}')
print(f'A comissão do vendedor ao vender a vista: R${comissao1:.2f}')
print(f'A comissão ao vender parcelado: R${comissao2:.2f}')
