from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar num número entre 0 e 5. Tente adivinhar...')
print('=-=' * 20)

mn = int(input('Em que número pensou? - '))

print('PROCESSANDO........')
sleep(3)

cn = randint(0, 5)

if mn == cn:
    print('Parabéns, Acertou no número!')
else:
    print('Pensei no número {} e não no número {}!'.format(cn, mn))
