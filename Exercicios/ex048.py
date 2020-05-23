som = 0
enc = 0

for c in range(3, 501, 3):
    if c % 2 == 1:
        enc += 1
        som += c

print('Foram encontrados {} números impares múltiplos de 3 entre 0 e 500 e a sua soma é de {}.'.format(enc, som))
