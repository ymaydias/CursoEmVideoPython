#Crie um programa que leia um numero inteiro e mostre na tela se ele eh par ou impar

numero = int(input('Digite um numero: '))
resultado = numero % 2

if resultado <= 0:
    print('Seu numero eh par')
else:
    print('Seu numero eh impar')