nom = str(input('Qual o seu nome completo? - ')).strip()

LNom = nom.split()

print('O seu primeiro nome é {}.'.format(LNom[0]))
print('O seu último nome é {}.'.format(LNom[len(LNom)-1]))
