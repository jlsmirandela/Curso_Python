nome = str(input('Digite o seu nome completo - ')).strip()

lista = nome.split()
sp = nome.count(' ')

print('O seu nome completo em maiúsculas é - ', nome.upper())
print('O seu nome em minúsculas é - ', nome.lower())
print('O seu nome tem {} letras'.format(len(nome) - sp))
print('O primeiro nome é "{}" e tem {} letras.'.format(lista[0], len(lista[0])))
