kh = int(input('Qual a velocidade do seu carro? - '))

if kh > 80:
    m = (kh - 80) * 7
    print('\033[31m'+'MULTADO. Ultramassou em {}Km/h o limite de 80Km/h. O valor da multa é de {:.2f}€'.format((kh - 80), m) + '\033[0;0m')
else:
    print('Está dentro do limite de velocidade.')
print('Bom dia e boa viagem')