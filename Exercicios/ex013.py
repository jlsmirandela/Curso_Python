Venc = float(input('Qual o valor do vencimento inicial (€) - '))
Aum = float(input('Qual a percentagem do aumento? - '))

print('Para um vencimento de {}€ com {}% de aumento ({:.2f}€) passará a ser de {:.2f}€.'.
      format(Venc, Aum, (Venc*Aum/100), (Venc+(Venc*Aum/100))))
