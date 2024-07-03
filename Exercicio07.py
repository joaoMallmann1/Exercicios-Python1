# Leia a temperatura em Fahrenheit e apresente-a convertida em Celsius
fahren = float(input('Digite o valor em Fahrenheit: '))
celsius = 5 * (fahren - 32)/9
print(f'{fahren} °F em Celsius: {round(celsius, 2)} °C')
