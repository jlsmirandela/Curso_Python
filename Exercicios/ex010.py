Eur = float(input('Quantos euros eu tenho - €'))
Tax = float(input('Qual a Taxa de Conversão - '))

print('Com {:.2f}€ consigo adquitir ${:.2f} Dólares.'.format(Eur, (Eur*Tax)))
