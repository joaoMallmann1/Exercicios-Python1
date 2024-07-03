# Leia um ângulo em graus e apresente-o convertido em radianos
import math

graus = float(input('Digite o valor em graus: '))
pi = math.pi
radianos = pi * graus / 180
print(f'{graus} graus em radianos são iguais a {round(radianos, 2)} radianos')
