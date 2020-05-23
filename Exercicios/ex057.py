sexo = str(input('Qual o seu sexo [M/F]? - ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Qual o seu sexo? - ')).strip().upper()[0]

if sexo == 'M':
    print('O seu sexo é masculino.')
else:
    print('O seu sexo é femenino')
