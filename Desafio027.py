# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

n = str(input('Escreva seu nome completo: ')).strip()

nome = n.split()

print(f'Seu primeiro nome eh {nome[0]}')
print(f'Seu ultimo nome eh {nome[len(nome)-1]}')