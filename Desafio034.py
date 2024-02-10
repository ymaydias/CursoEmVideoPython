# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para salario superiores a R$1250, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento eh de 15%

salario = float(input('Qual eh seu salario atualmente?: '))
aumento = salario * 1.15 if salario <= 1250 else salario * 1.10

print(f'Seu salario com aumento sera {aumento}')