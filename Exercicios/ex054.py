from datetime import date

maior = 0
menor = 0
ano = date.today().year

for c in range(1, 8):
  dnasc = int(input('Em que ano nasceu a {}ª pessoa? - '.format(c)))
  if dnasc + 18 >= ano:
      maior += 1
  else:
      menor += 1

print('\nAo todo tivemos {} maiores de idade e {} menores de idade'.format(maior, menor))
