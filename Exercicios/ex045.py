from random import randint
from time import sleep

items = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)

print('''Suas opções:
[ 0 ] PAPEL
[ 1 ] PEDRA
[ 2 ] TESOURA''')
jog = int(input('Qual a sua jogada? - '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=-' * 10)
print(' O computador jogou {}.'.format(items[comp]))
print(' O jogador jogou {}.'.format(items[jog]))
print('-=-' * 10)

if comp == 0:   # Pedra
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('JOGADOR VENCE')
    elif jog == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Inválida')
elif comp == 1: # Papel
    if jog == 0:
        print('COMPUTADOR VENCE')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada Inválida')
elif comp == 2: # Tesoura
    if jog == 0:
        print('JOGADOR VENCE')
    elif jog == 1:
        print('COMPUTADOR VENCE')
    elif jog == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida')
print('-=-' * 10)
