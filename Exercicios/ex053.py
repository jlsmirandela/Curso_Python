frase = str(input('Digite uma frase - ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))

#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
if junto == inverso:
    print('É palíndromo!')
else:
    print('Não é palíndromo.')
