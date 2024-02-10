# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porcao inteira

import  math

n = float(input('Digite um numero real: '))
nint = math.trunc(n)

print(f'O numero {n} tem a parte inteira de {nint}')



