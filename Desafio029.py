# Escreva um programa que leia a velocidade de um caroo. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada KM acima do limite

kmh = float(input('A quantos km/h vc esta dirigindo? '))

if kmh > 80:
    print('Vc esta dirigindo acima da velocidade permitida!')
    print(f'Voce sera multado! A multa custara R${(kmh-80)*7}')
print('Tenha uma boa viagem, sempre siga as leis de transito')
