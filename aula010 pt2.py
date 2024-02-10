# Condissoes simples e condicoes compostas

#       CONDICAO
# if carro.esquerda():
#   bloco True
# else:
#   bloco False

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) /2
print(f'Sua media foi {m}')

if m >= 6.0:
    print('Parabens, vc passou!')
else:
    print('Voce nao passou...')