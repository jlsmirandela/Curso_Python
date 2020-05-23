val = float(input('Qual o valor das compras? (€) - '))

print('** FORMAS DE PAGAMENTO **')

fp = int(input('[ 1 ] à vista dinheiro/Cheque \n'
               '[ 2 ] à vista cartão \n'
               '[ 3 ] 2x no cartão \n'
               '[ 4 ] 3x ou mais no cartão \n'
               ' - Qual a opção? - '))

if 1 <= fp <= 4:
    if fp == 1:
        print('A compra tem um valor de {:.2f} tendo um desconto de {:.2f}€ (10%) ficando com o valor de {}€.'.format(val, (val * 0.1), val-(val*0.1)))
    elif fp == 2:
        print('A compra tem um valor de {:.2f} tendo um desconto de {:.2f}€ (5%) ficando com o valor de {}€.'.format(val, (val * 0.05), val-(val*0.05)))
    elif fp == 3:
        print('A compra tem um valor de {:.2f} não tendo qualquer desconto ou agravamento'.format(val))
        print('Ficará a pagar {:.2f}€ por prestação.'.format(val / 2))
    elif fp == 4:
        np = int(input("Qual o numero de prestações? - "))
        prest = (val + (val * 0.2)) / np
        print('A compra tem um valor de {:.2f} tendo um agravamento de {:.2f}€ (20%) ficando com o valor de {:.2f}€.'.format(val, (val*.2), val + (val * 0.2)))
        print('Ficará a pagar {:.2f}€ por prestação.'.format(prest))
else:
    print('Opção de pagamento não válida!')
