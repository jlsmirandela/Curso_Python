T = int(input('Digite um número para ver a tabuada - '))

print('-'*12)
for c in range(1, 11):
    print("{} x {:2} = {}".format(T, c, T * c))
print('-'*12)