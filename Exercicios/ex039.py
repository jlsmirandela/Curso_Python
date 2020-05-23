from datetime import date

nasc = int(input('Qual a data de nascimento? - '))
Sexo = str(input('Sexo ([M - F] - ')).strip().upper()

anact = date.today().year
idade = anact - nasc

if idade < 18 and Sexo == 'M':
    print('Ainda lhe faltam {} anos para o alistamento que deverá efectuar em {}.'.format(anact-nasc, 18 - idade + anact))
elif idade > 18 and Sexo == 'M':
    print('Já deveria ter efectuado o seu alistamento em {} passando já {} anos.'.format(nasc + 18, anact - (nasc + 18)))
elif idade == 18 and Sexo == 'M':
    print('Deverá alistar-se imediatamente')
elif Sexo == 'F':
    print('Está dispensado do serviço militar')
else:
    print('Sexo Indefinido')
