num = int(input('Digite um número - '))
contd = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\33[32m'+ str(c) + '\33[0;0m', end=' ')
        contd += 1
    else:
        print('\33[31m'+ str(c) + '\33[0;0m', end=' ')
if contd <= 2:
    print('\nO número {} é PRIMO!!!'.format(num))
else:
    print('\nO número não é primo.'.format(num))
