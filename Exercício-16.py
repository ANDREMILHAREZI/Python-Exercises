### Faça a leitura de 3 valores e apresente como resultado a soma dos quadrados dos três valores lidos ###

v1 = float(input('Valor 1:  '))
v2 = float(input('Valor 2:  '))
v3 = float(input('Valor 3:  '))
qv1 = (v1 ** 2)
qv2 = (v2 ** 2)
qv3 = (v3 ** 2)

qvt = (qv1 + qv2 + qv3)
print (f'O valor da soma dos quadrados é {qvt}')
