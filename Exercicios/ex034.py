sal = int(input('Qual o salário? - '))

if sal >= 1250:
    print('O salário superior a 1250€ terá um aumento de 10% passando a receber {:.2f}€'.format((sal * 10 / 100) + sal))
else:
    print('O salário inferior a 1250€ terá um aumento de 15% passando a receber {:.2f}€'.format((sal * 15 / 100) + sal))
