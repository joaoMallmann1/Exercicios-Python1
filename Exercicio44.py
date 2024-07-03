"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mos
tre quantos degraus o usuário deverá subir para atingir seu objetivo
"""
import math


altura_degrau = float(input("Digite a altura do degrau: "))
altura_usuario = float(input("Digite a altura que o usuário deseja alcançar na escada: "))
numero_degraus = altura_usuario / altura_degrau
numero_degraus = math.ceil(numero_degraus)

print(f'O usuário deverá subir {numero_degraus} degraus para alcançar a altura desejada.')
