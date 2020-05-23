peso = float(input('Indique o seu peso (Kg) - '))
alt = float(input('Indique a sua altura (m) - '))

IMC = peso / (alt ** 2)

if IMC <= 18.5:
    print('O seu IMC é de {:.1f} e está com EXCESSO DE MAGREZA.')
elif 18.5 < IMC <= 25:
    print('O seu IMC é de {:.1f} e está com PESO NORMAL')
elif 25 < IMC <= 30:
    print('O seu IMC é de {:.1f} e está com EXCESSO DE PESO'.format(IMC))
elif 30 < IMC <= 35:
    print('O seu IMC é de {:.1f} e está com OBESIDADE GRAU I'.format(IMC))
elif 35 < IMC <= 40:
    print('O seu IMC é de {:.1f} e está com OBESIDADE GRAU II'.format(IMC))
else:
    print('O seu IMC é de {:.1f} e está com OBESIDADE GRAU III'.format(IMC))
