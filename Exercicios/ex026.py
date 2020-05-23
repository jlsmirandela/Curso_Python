fr = str(input('Digite uma frase - ')).strip()

FR = fr.upper()

print('A letra "A" apareceu {} vezes.'.format(FR.count('A')))
print('A primeira letra "A" apareceu na posição {}.'.format(FR.find('A') + 1))
print('o último "A" apareceu na posição {}.'.format(FR.rfind('A') + 1))
