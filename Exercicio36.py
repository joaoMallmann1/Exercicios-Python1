"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
"""
import math

altura = float(input('Digite a altura do cilindro: '))
raio = float(input('Digite o raio do cilindro: '))

volume = math.pi * (raio ** 2) * altura
print(f'O volume de um cilindro com a altura de {altura:.2f} e raio de {raio:.2f} é igual a {volume:.2f}')
