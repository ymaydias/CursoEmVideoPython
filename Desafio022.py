# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas e minusculas
# Quantas letras ao todo (sem considerar espacos)
# Quantas letras tem o primero nome

nome = str(input('Qual seu nome completo? '))
nomemaius = nome.upper()
nomeminus = nome.lower()
nome1 = nome.split()
quantidade = len(nome1[0])
semespaco = nome.strip()
quantidadesem = len(semespaco) - semespaco.count(' ')

print(f'Seu nome maiusculo e minusculo ficam {nomemaius} e {nomeminus}')
print(f'Seu nome inteiro, sem espacos, possui {quantidadesem} letras')
print(f'Seu primeiro nome possui {quantidade} letras')