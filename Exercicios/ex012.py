Val = float(input('Qual o valor inicial do produto (€) - '))
Des = float(input('Qual a percentagem de desconto? - '))

print('O produto que tinha o valor inicial de {:.2f}€, com {}% de desconto passará a custar {:.2f}€.'.format(Val, Des, (Val - (Val*Des/100))))
