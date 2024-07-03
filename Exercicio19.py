# Leia um valor em litros e apresente-o convertido em metros cúbicos
litros = float(input('Digite um volume em litros: '))
m3 = litros / 1000
print(f'{litros} L em metros cúbicos são iguais a {round(m3, 2)} metros cúbicos')
