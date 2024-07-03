# Leia um valor de comprimento em centimetros e apresente-o convertido em polegadas
cm = float(input('Digite um comprimento em centímetros: '))
pol = cm/2.54
print(f'{cm} cm em polegadas são iguais a {round(pol, 2)} pol')
