cont = 1
num = 0

while True:
    print('-'*40)
    num = int(input('Quer ver a tabuada de que valor? - '))
    if num < 0:
        break
    print ('-'*40)
    for cont in range(1, 11):
        print(f'{num} x {cont:2} = {num * cont}')
    cont = 1
