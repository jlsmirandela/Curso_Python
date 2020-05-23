n1 = int(input('Insira o primeiro número - '))
n2 = int(input('insira o segundo número - '))
n3 = int(input('Indira o terceiro número - '))

lista = [n1, n2, n3]
lista.sort()

print('O menor número digitado foi - {}'.format(lista[0]))
print('O maior número digitado foi - {}'.format(lista[2]))
