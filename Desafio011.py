# Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m2

largura = float(input('Quanto de largura possui sua parede? '))
altura = float(input('Quanto de altura possu sua parede? '))

area = (largura*altura)
tinta = (area/2)

print(f'A area de sua parede eh de {area}m2, para essa area eh necessario {tinta} litros de tinta')

