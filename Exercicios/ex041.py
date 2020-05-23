from datetime import date

nasc = int(input('Qual a data de nascimento? - '))

idade = (date.today().year) - nasc

if idade <= 9:
    print('O atleta tem {} anos e é categoria MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e é categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e é categoria JÚNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e é categoria SÉNIOR'.format(idade))
else:
    print('O atleta tem {} anos e é categoria MASTER'.format(idade))