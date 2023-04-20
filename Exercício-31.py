num = int(input('Digite o número: '))
while num < 1000 or num > 9999:
  print ('Digite um num valido')
  num = int(input())
digito = str(num)
print (digito[0])
print (digito[1])
print (digito[2])
print (digito[3])