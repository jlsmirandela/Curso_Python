Alt = float(input('Qual a altura da parede (m) - '))
Com = float(input('Qual o comprimento da parede (m) - '))
Rend = float(input('Qual o rendimento a tinta (l/m²) - '))
Area = Alt * Com

print('\n Para uma parede de {}m x {}m (que dá {}m²] necessita {:.1f}l de tinta'.format(Alt, Com, Area, (Area*Rend)))
