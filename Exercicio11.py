# Leia uma velocidade em m/s e apresente-a convertida em hm/h
metro = float(input("Digite uma velocidade em metros: "))
km = metro * 3.6
print(f'{metro} m/s são iguais a {round(km, 2)} km/h')
