algo = input('Digite algo - ')

print('O tipo primitivo de "{}" é '.format(algo), type(algo))
print('Só tem espaços?', (algo.isspace()))
print('É um número?', (algo.isnumeric()))
print('É alfabético?', (algo.isalpha()))
print('É alfanumérico?', (algo.isalnum()))
print('Está em maiúsculas?', (algo.isupper()))
print('Está em minísculas?', (algo.islower()))
print('Está capitalizado?', (algo.istitle()))