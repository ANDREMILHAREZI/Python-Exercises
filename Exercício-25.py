# Faça um programa que solicite o número de dias trabalhados pelo funcionário e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda e a empresa paga R$30,00 o dia trabalhado#

qtd = int(input('Quantidade de dias trabalhados:  '))
d =  30
pg = d * qtd
ir = pg * 0.08


t = pg - ir

print (f'Irá receber a quantia de R$ {t}')