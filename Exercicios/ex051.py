print('*-' * 20)
print('   PROGRESSÃO ARITMÉTICA - 10 TERMOS')
print('*-' * 20)

pt = int(input('Primeiro termo : '))
rz = int(input('Razão: '))
val = pt

for c in range(1, 11):
    print(val, '→', end=' ')
    val += rz

print('!FIM!')
