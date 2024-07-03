"""
Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite o número de dias trabalhados
pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto
de renda
"""
diaria = 30.00
qtd = int(input('Quantos dias o encanador trabalhou? '))

valor_bruto = diaria * qtd
valor_liquido = valor_bruto - (valor_bruto * 0.08)

print(f'O valor bruto da diária do encanador é de R${valor_bruto:.2f} e o líquido de R${valor_liquido:.2f}')
