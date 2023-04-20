<<<<<<< HEAD
#### A importância de r$780.000 será dividida entre três ganhadores  de um concurso.####
####  Sendo que da quantia total total: ####
#### O primeiro ganhador receberá 46%, ####
#### O segundo receberá 32 %, ####
# O terceiro receberá o restante, #
# Calcule e imprima a quantia ganha por cada um dos ganhadores #

p = int(input('Prêmio do concurso:  '))
g = p * 0.46
s = p * 0.32
t = p * 0.22

print (f'O ganhador receberá R${g} , o segundo colocado receberá R${s} , o terceiro colocado receberá R${t}')
=======
# Faça um programa que solicite o número de dias trabalhados pelo funcionário e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda e a empresa paga R$30,00 o dia trabalhado#

qtd = int(input('Quantidade de dias trabalhados:  '))
d =  30
pg = d * qtd
ir = pg * 0.08


t = pg - ir

print (f'Irá receber a quantia de R$ {t}')
>>>>>>> 20c6ee0a1c4ad4d607ee2c8abbb255cb0aa7a7d3
