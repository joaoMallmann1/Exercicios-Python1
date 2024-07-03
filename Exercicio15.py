# Leia um ângulo em radianos e apresente-o convertido em graus
import math

radianos = float(input('Digite o valor em radianos: '))
pi = math.pi
graus = radianos * 180/pi
print(f'{radianos} radianos em graus são iguais a {round(graus, 2)}')
