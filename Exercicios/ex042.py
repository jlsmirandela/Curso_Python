print('-=' * 20)
print('ANALIZADOR DE TRANGULOS')
print('-=' *20)

l1 = float(input('Primeiro segmento - '))
l2 = float(input('Segundo segmento - '))
l3 = float(input('Terceiro segmento - '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('PODE FORMAR TRIÂNGULO!!!!!!')
    if l1 == l2 == l3:
        print('O triângulo é equilálero.')
    elif l1 != l2 != l3 != l1:
        print ('O triângulo é escaleno')
    else:
        print('O triângulo é Isósceles.')
else:
    print('Não pode formar triângulo.')

print('-=' * 20)
