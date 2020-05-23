F = True
Cont = int(0)
Med = float(0)
Max = int(0)
Min = int(0)

while F:
    num = int(input('Digite um número: '))
    flag = str(input('Deseja continuar? [S/N] - ')).strip().upper()[0]
    if flag == 'S':
        F = True
    elif flag == 'N':
        F = False
    else:
        flag = str(input('Opção incorrecta. Deseja continuar? [S/N]')).strip().upper()[0]
    Cont += 1
    if num > Max:
        Max = num
    if Cont == 1:
        Med = num
        Min = num
    else:
        Med = (Med + num) / 2
        if num < Min:
            Min = num
print('Foram digitados {} números sendo a sua média de {:.1f}.'.format(Cont, Med))
print('O maior valor foi {} e o mínimo foi {}'.format(Max, Min))


