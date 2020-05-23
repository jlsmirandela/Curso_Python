from math import sqrt, hypot

co = float(input('Qual o comprimento do cateto oposto? - '))
ca = float(input('Qual o comprimento do cateto adjacente? - '))
ct = (co**2) + (ca**2)
ht = sqrt(ct)

print('Para um triangulo rectângulo cujos catetos medem {} e {}, a sua hipotnusa mede {:.3f}.'.format(co, ca, ht))
print('Para um triangulo rectângulo cujos catetos medem {} e {}, a sua hipotnusa mede {:.3f}.'.format(co, ca, hypot(co, ca)))

