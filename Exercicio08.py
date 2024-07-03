# Leia a temperatura em Kelvin e apresente-a convertida em Celsius
kelvin = float(input('Digite o valor em Kelvin: '))
celsius = kelvin - 273.15
print(f"{kelvin} graus em Celsius: {round(celsius,2)} °C")
