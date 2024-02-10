# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule entao o preco a pagar
# sabendo que o carro custa R$60 por dia e R$0.15 por km rodado

km = float(input('Quantos KM foram rodados com o carro? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
preco = (km*0.15)+(dias*60)

print(f'Com as informacoes dadas, foi calculado e o aluguel saira por R${preco:.2f}')