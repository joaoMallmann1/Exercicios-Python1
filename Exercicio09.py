# Leia a temperatura em Celsius e apresente-a convertida em Kelvin
celsius = float(input('Digite a temperatura em Celsius: '))
kelvin = celsius + 273.15
print(f'{celsius} °C em Kelvin é igual a {round(kelvin, 2)}')
