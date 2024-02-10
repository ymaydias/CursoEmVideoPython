# Faca um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'
# Em que posicao ela aparece a primeira vez
# Em que posicao ela aparece a ultima vez

frase = str(input('Escreva uma frase qualquer: ')).upper().strip()


print(f'Nesta frase a letra A aparece {frase.count("A")} vezes')
print(f'A primeira vez que a letra A apareceu foi na posicao {frase.find("A")+1}')
print(f'A segunda vez que a letra A apareceu foi na posicao {frase.rfind("A")+1}')