from math import factorial

print('Cálculo factorial')
n = int(input('Indique um número - '))
f = 1

print('O factorial de {}! é '.format(n), end='   ')
while n > 0:
    print(n, end=' ')
    print(' x ' if n > 1 else ' = ', end= ' ')
    f *= n
    n -= 1
print(f)