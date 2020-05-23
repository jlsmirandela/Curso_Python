from random import randint

comp = randint(0, 10)
tent = 1

print('Sou o seu computador....')
print('Acabei de pensar num número entre 0 e 10. Tente adivinhar!')

jog = int(input('\nQual a sua aposta? - '))

while jog != comp:
    if jog < comp:
        jog = int(input('Mais, tente de novo - '))
        tent += 1
    else:
        jog = int(input('Menos, tente de novo - '))
        tent += 1

if tent == 1:
    print('Parabéns, Acertou à primeira!!!')
else:
    print('Parabéns, acertou à {}ª tentativa'.format(tent))
