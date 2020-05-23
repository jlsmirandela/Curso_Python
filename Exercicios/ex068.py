from random import randint

comp = randint(0, 5)
jog = 0
soma = 0
par = True

print('=-' *20)
print('      Vamos jogar Par ou Ímpar ' )
print('-=' *20)
while True:
    jog = int(input('Diga um valor (0 - 5) - '))
    opcao = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    if opcao != 'P' and opcao != 'I':
        opcao = str(input('Opção errada. Par ou Ímpar? [P/I]')).strip().upper()[0]
    soma = comp + jog
    if soma % 2 == 0:
        par = True
    else:
        par = False
    print('-' *40)

