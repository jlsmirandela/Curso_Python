vcasa = int(input('Qual o valor da casa? - '))
vsal = int(input('Qual o seu salário? -'))
anos = int(input('Durante quantos anos pretende pagar? - '))

pmes = vcasa / anos * 12
esf = pmes * 100 / vsal

print('Para compara uma casa de {:.2f}€ durante {} anos a prestação mensal será de {:.2f}€.'.format(vcasa, anos, pmes))
if esf < 30:
    print('Empréstio CONCEDIDO!!!!')
else:
    print('Empréstimo NEGADO.')
