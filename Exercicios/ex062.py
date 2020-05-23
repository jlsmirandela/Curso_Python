print('-+-' *10)
print('       GERADOR DE PA')
print('+-+' * 10)

c = 1  # Contador de ciclos
rep = 1
nter = 1


ter = int(input('Insira o primeiro termo - '))
rz = int(input('Insira a razão - '))

while c <= 10:
    print(ter, ' → ', end=' ')
    ter += rz
    c += 1
    nter += 1
print('PAUSA')

while rep != 0:
    c = 1
    rep = int(input('Quantos termos mais? - '))
    while c <= rep:
        print(ter, ' → ', end=' ')
        ter += rz
        c += 1
        nter += 1

print('Progressãp finalizada com {} termos.'.format(nter - 1))
