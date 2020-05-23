pv = int(input('Insira o primeiro valor - '))
sv = int(input('Insira o segundo valor - '))
op = 0

while op != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair''')
    op = int(input('>>>>>>>>  Qual a sua opção? - '))
    while op not in range(0, 6):
        op = int(input('Opção inválida, escolha uma opção? - '))
    if op == 1:
        print('A soma entre {} e {} é {}.\n'.format(pv, sv, pv + sv))
    elif op == 2:
        print('A multiplicação entre {} e {} é {}\n'.format(pv, sv, pv * sv))
    elif op == 3:
        if pv > sv:
            print('O primeiro valor ({}) é MAIOR que o segundo valor ({})\n'.format(pv, sv))
        elif pv < sv:
            print('O segundo valor ({}) é MAIOR que o primeiro valor ({}\n)'.format(sv, pv))
        else:
            print('Os valores são IGUAIS.\n')
    elif op == 4:
        pv = int(input('Insira o primeiro valor - '))
        sv = int(input('Insira o segundo valor - '))

print('Fim do programa')

