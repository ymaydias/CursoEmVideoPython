# Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto

valor = float(input('Qual o valor do produto? R$'))

desconto = (valor * 0.05)

valorfinal = (valor - desconto)

print(f'R${valor} com 5% de desconto ficara R${valorfinal:.2f}')
