"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro
"""
num = int(input("Digite um valor inteiro qualquer: "))
soma = ((num * 3) + 1) + ((num * 2) - 1)
print(f'A soma do sucessor do triplo de {num} mais o antecessor de seu dobro é igual a {soma}')
