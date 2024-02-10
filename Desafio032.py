# Faca um programa que leia um ano qualquer e mostre se ele eh bissexto

from    datetime import date

ano = int(input('Digite qualquer ano e diremos se ele eh bissexto ou nao: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} eh bissexto')
else:
    print(f'O ano {ano} nao eh bissexto')