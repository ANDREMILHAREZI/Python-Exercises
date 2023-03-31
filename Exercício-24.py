### Leia um salário. Calcule e imprima o valor do novo salário sabendo que receberá 25% a mais ###


salario = float(input('Digite o salário do funcionário:  '))
porc = salario * 0.25
ajuste = salario + porc

print (f'O novo salário do funcionário é {ajuste} reais')