num = int(input('\033[35m' + 'Insira um número - ' + '\033[0;0m'))

if num % 2 == 0:
    print('\033[32m' + 'O número é par.' + '\033[0;0m')
else:
    print('\033[31m' + 'O número é impar.' + '\033[0;0m')
