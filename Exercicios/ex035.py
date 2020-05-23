print('-=' * 20)
print('ANALIZADOR DE TRANGoLOS')
print('-=' *20)

l1 = float(input('Primeiro segmento - '))
l2 = float(input('Segundo segmento - '))
l3 = float(input('Terceiro segmento - '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('PODE FORMAR TRIÂNGULO!!!!!!')
else:
    print('Não pode formar triângulo.')

print('-=' * 20)
