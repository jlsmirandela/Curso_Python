num = 0
cont = 0
som = 0

while True:
    num = int(input('Digite um valor (999 para parar - '))
    if num == 999:
        break
    cont += 1
    som += num
print(f'A soma dos {cont} valores foi de {som}.')
