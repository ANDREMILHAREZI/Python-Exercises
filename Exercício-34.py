#Insira o valor de cada concorrente#
v1 = float(input())
v2 = float(input())
v3 = float(input())
premio = float(input())

#valor total das 3 apostas dos concorrentes#
total_investido = v1+v2+v3 

#valores investidos de cada concorrente, dividido pelo total investido entre eles#

percentual1 = v1/total_investido
percentual2 = v2/total_investido
percentual3 = v3/total_investido

#percentual do valor investido, multiplicado pelo premio#

valor_premio1 = percentual1*premio
valor_premio2 = percentual2*premio 
valor_premio3 = percentual3*premio 

print (f'O primeiro apostador ganharia {valor_premio1}')
print (f'O segundo apostador ganharia {valor_premio2}')
print (f'O terceiro apostador ganharia {valor_premio3}')