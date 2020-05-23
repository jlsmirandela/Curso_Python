print('-+-' *10)
print('       GERADOR DE PA')
print('+-+' * 10)

c = 1

ter = int(input('Insira o primeiro termo - '))
rz = int(input('Insira a razão - '))

while c <= 10:
    print(ter, ' → ', end=' ')
    ter += rz
    c += 1

print('FIM')

