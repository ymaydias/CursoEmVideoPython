# Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input('Digite um numero: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'A unidade deste valor eh: {u}')
print(f'A dezena deste valor eh: {d}')
print(f'A centena deste valor eh: {c}')
print(f'O milhar deste valor eh: {m}')
