num = int(input('Insira um número inteiro - '))

print('Escolha a base de conversão:')
esc = int(input('[ 1 ] - Converter para BINARIO \n[ 2 ] - Converter para OCTAL \n[ 3 ] - Converter para HEXADECIMAL '))

if esc == 1:
    print('O número {} convertido para BINÁRIO é "{}"'.format(num, bin(num)[2:]))
elif esc == 2:
    print('O número {} convertido para OCTAL é "{}"'.format(num, oct(num)[2:]))
elif esc == 3:
    print('O número {} convertido para HEXADECIMAL é "{}"'.format(num, hex(num)[2:]))
else:
    print('A opção não está correcta.')
