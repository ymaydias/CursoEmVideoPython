# O mesmo professor do desafo anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print('A ordem da apresentacao sera')
print(lista)
