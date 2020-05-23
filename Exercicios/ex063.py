print('- ' * 20)
print('      SEQUÊNCIA DE FIBONACCI')
print('- ' * 20)

c = 3
t1 = 0
t2 = 1
t3 = 0

nt = int(input('Quantos termos quer mostrar? - '))
print('{} → {}'.format(t1, t2), ' → ', end=' ')
while c <= nt:
    t3 = t1 + t2
    print(t3, ' → ', end= ' ')
    t1 = t2
    t2 = t3
    c += 1

print('FIM')


