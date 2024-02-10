# Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome 'Santo'

cid = str(input('Qual sua cidade de nascimento?: ')).strip()

print(cid[:5].upper() == 'SANTO')