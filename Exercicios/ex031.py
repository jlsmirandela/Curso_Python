via = int(input('Indique o número de Kms - '))

if via <= 200:
    print('A viagem tem um custo de {:.2f}€.'.format(via * 0.50))
else:
    print('A viagem tem um custo de {:.2f}$'.format(via * 0.45))

print('\nCusto da viagem é de {:.2f}€'.format(via * 0.50 if via <= 200 else via * 0.45))
