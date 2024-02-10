# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo e mostre o comprimento da hipotenusa

from    math    import  hypot

co = float(input('Digte o comprimento do cateto oposto: '))
ca = float(input('Digte o comprimento do cateto adjcente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')