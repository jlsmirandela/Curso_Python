nota1 = float(input('Insira a primeira nota - '))
nota2 = float(input('Insira a segunda nota - '))

med = (nota1 + nota2) / 2

if med < 5:
    print('Média - {:.1f} - REPROVADO'.format(med))
elif 5 <= med < 7:
    print("Média - {:.1f} - PARA RECUPERAÇÂO.".format(med))
else:
    print ('Média - {:.1f} - APROVADO!'.format(med))