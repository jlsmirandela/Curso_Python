soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite o {}º número - '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Foram digitados {} números pares sendo a sua soma de {}.'.format(cont, soma))
