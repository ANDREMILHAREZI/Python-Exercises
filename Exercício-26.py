##  Receba o salário de um funcionário. Se sabe que o mesmo receberá 5% de gratificação e pagou 7% de imposto. Imprima quanto ele recebeu ao final ##


sal = float(input('Salário do funcionário:  '))
gt = sal * 0.02
im = sal - gt

print(f'O salário será de R$ {im}')
