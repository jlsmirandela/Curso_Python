from math import radians, cos, sin, tan

ang = float(input('Digite um ângulo pretendido - '))
angr = float(radians(ang))

print('O SENO de {}° é {:.2f}'.format(ang, sin(angr)))
print('O COSENO de {}° é {:.2f}'.format(ang, cos(angr)))
print('A TANGENTE de {}° é {:.2f}'.format(ang, tan(angr)))
