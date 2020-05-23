Dal = int(input('Quantos dias o carro foi alugado? - '))
Kal = int(input('Quantos Kilometros andou?'))
VDal = float(Dal*60)
VKal = float(Kal * 0.15)

print('A viatuta foi alugada por {} dias tendo custado {:.2f}€.'.format(Dal, VDal))
print('A viatura andou {}Km tendo custado {:.2f}€.'.format(Kal, VKal))
print('O valor final do aluguer é de {:.2f}€.'.format(VDal + VKal))
