"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raiz de a ao quadrado + b ao quadrado.
Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação. Imprima então
o resultado
"""
import math

a = float(input('Digite o valor do cateto a do triângulo: '))
b = float(input('Digite o valor do cateto b do quadrado: '))
soma = (a**2 + b**2)
hipotenusa = math.sqrt(soma)
print(f'A hipotenusa do triângulo é igual a {hipotenusa:.2f}')
