# Leia uma distância em milhas e apresente-a convertida em km
milhas = float(input("Digite uma distância em milhas: "))
km = 1.61 * milhas
print(f'{milhas} milhas em quilômetros são iguais a {round(km, 2)} km')
