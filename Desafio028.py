# Escreva um programa que faca o computador 'pensar' em um numero inteiro entre entre 0 e 5 para o usuario tentar descobrir qual foi
# o numero escolhido pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu

import random

n = int(input('Estou pensando em um numero de 1 a 5, qual eh? '))

n1 = [1, 2, 3, 4, 5]

random.shuffle(n1)

n2 = n1[0]

if n == n2:
    print(f'Vc acertou! Estava pensando no numero {n2}')
else:
    print(f'Vc errou, nao estava pensando no numero {n}')
    print(f'Estava pensando no numero {n2}')

# from random import randint
#from time import sleep

#computador = randint(0, 5)
#print = ('-=-' * 20)
#print ('Vou pensar em um numero entre 0 e 5. Tente adivinhar... ')
#print = ('-=-' * 20)
#jogador = int(input('Em que numero eu pensei?))
#print ('PROCESSANDO...)
#if jogador == computador:
#   print('Parabens! Voce conseguiu me vencer!)
#else:
#   print(f'Ganhei! Eu pensei no numero {computador} e nao no {jogador}!)