TIdade = 0
NMV = ''
IHV = 0
NH = 0
NM = 0

for c in range(1, 5):
    print('\n----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome - ')).strip()
    idade = int(input('Idade - '))
    sexo = str(input('Sexo [M/F] - ').strip()).upper()
    if sexo != 'M' and sexo != "F":
        print('Sexo Indefinido')
    TIdade += idade
    if c == 1:
        if sexo == 'M':
            NMV = nome
            IHV = idade
            NH += 1
        else:
            if idade < 20:
                NM += 1
    else:
        if sexo == 'M':
            NH += 1
            if idade > IHV:
                NMV = nome
                IHV = idade
        else:
            if idade < 20:
                NM += 1

print('A média de idade do grupo é de {:.0f} anos.'.format(TIdade / c))
if IHV != 0:
    print('O homem mais velho tem {} anos e chama-se {}.'. format(IHV, NMV))
else:
    print('Não existem homens nesta lista.')
print('No grupo existem {} mulheres com menos de 20 anos.'. format(NM))
