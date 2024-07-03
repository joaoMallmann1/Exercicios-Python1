"""
Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área do dírculo é π =
raio ao quadrado.
"""
import math

raio = float(input('Digite o valor do raio de um círculo: '))
area = math.pi * (raio ** 2)

print(f'A área do círculo com raio {raio} é {area:.2f}')
