### Programa que leia o valor de um produto e imprima o valor com desconto de 12% ###

produto = float(input('Digite o valor do produto: R$ '))

desc = produto * 0.12
final = produto - desc
print (f'O valor do produto com desconto de 12% é: R$ {final}   ')
