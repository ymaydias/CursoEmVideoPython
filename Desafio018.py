# Faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo que deseja '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O angulo desejado {angulo} possui a seno de {seno:.2f}')
print(f'O angulo desejado {angulo} possui a cosseno de {cosseno:.2f}')
print(f'O angulo desejado {angulo} possui a tangente de {tangente:.2f}')
