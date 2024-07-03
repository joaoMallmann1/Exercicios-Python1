# Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor em dólar
real = float(input('Digite um montante em reais: '))
cotacao = float(input('Digite a cotação atual do dólar: '))
dolar = real / cotacao
print(f'Na atual cotação, R$ {real} em dólares são iguais a {dolar:.2f} $')
