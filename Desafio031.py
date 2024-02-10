#Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preco da passagem, cobrando R$0,50 por KM para viagens ate 200km e R$0,45 para viagens mais
#longas

km = float(input('Quantos KM sera sua viagem?: '))

if km <= 200:
    print(f'Sua passagem custara {km * 0.50}')
else:
    print(f'Sua passagem custara {km * 0.45}')

#preco = km * 0.50 if km <= 200 else km * 0.45