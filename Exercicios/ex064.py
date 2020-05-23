c = 0
n = 0
sum = 0

while n != 999:
    n = int(input('Insira um número [999 para fim] - '))
    if n != 999:
        sum = sum + n
        c += 1

print('Digitou {} números sendo a sua soma igual a {}.'.format(c, sum))
